from google.appengine.ext import db

# PK = pubmed_id
class study(db.Model):
    # 3
    date = db.DateProperty(required=True)
    # 1 - private key
    pubmed_id = db.IntegerProperty(required=True)
    # 5
    pubmed_url = db.LinkProperty()
    # 6 - description of study
    name = db.StringProperty(required=True)
    # 7 disease or trait researched
    disease_trait = db.StringProperty(required=True)
    
    abstract = db.StringProperty()

    # 8 - antal forsøgspersoner
    init_sample_size = db.StringProperty()
    # 9
    repl_sample_size = db.StringProperty()

    # 10
    # region = db.StringProperty()
    # 12
    # chr_position = db.IntegerProperty()
    # 13
    # r_gene = db.StringProperty() # reported gene
    # mapped gene: 14
    # m_gene = db.StringProperty()
    # 18
    # upstream_gene = db.StringProperty()
    # 19
    # downstream_gene = db.StringProperty()
    # 20
    # snp_allele = db.StringProperty()
    # 21
    
    # 31 - copy number variations
    # CNV = db.StringProperty()
    # # 32 - ??
    # Platform = db.StringProperty()

# ID = random
# ancestor=study_id == pubmed_id
class gwas(db.Model):
    # maybe ancestor instead?
    # - improves consistency in high replication data store
    study = db.ReferenceProperty(study, required=True)

    # if the snp is _in_ a specific gene - this is the id
    gene = db.ReferenceProperty(gene)
    # if not, these two contain the reference-ids
    upstream = db.ReferenceProperty(gene)
    downstream = db.ReferenceProperty(gene)

    snps = db.ReferenceProperty(snp)
    # 27 - 
    p_string = db.StringProperty()
    # 6 * 10^-8 => p_val = -8
    p_val = db.IntegerProperty() 
    # 30 - Odds ratio #.##
    OR_beta = db.FloatProperty()
    # 26 - #.##
    riscAlleleFrequency = db.FloatProperty()
    # 25 - 1=no, 2=yes
    intergenic = db.BooleanProperty()

# id NCBI gene_id
# handle relations with ancestors
class gene(db.Model):
    studies = db.ListProperty(db.Key) # or simply pubmed_ids..
    alias = db.StringListProperty()
    name = db.StringProperty(required=True)
    geneid = db.IntegerProperty(required=True)

# id = SNPID
class snps(db.Model):
    studies = db.ListProperty(db.Key)
    gene = db.ReferenceProperty(gene, required=True)
    id = StringProperty(required=True) # rs1805007
    studies = db.ListProperty(db.Key)