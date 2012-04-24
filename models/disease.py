from google.appengine.ext import db

# SNP models:
class gwas(db.Model):
    """
    DATE ADDED TO CATALOG: Date added to catalog 
    PUBMEDID: PubMed identification number 
    FIRST AUTHOR: Last name of first author 
    DATE: Publication date (online (epub) date if available) 
    JOURNAL: Abbreviated journal name 
    LINK: PubMed URL
    STUDY: Title of paper (linked to PubMed abstract) 
    DISEASE/TRAIT: Disease or trait examined in study 
    INITIAL SAMPLE SIZE: Sample size for Stage 1 of GWAS 
    REPLICATION SAMPLE SIZE: Sample size for subsequent replication(s) 
    CYTOGENETIC_LOC: Cytogenetic region associated with rs number (NCBI) 
    CHR_ID: Chromosome number associated with rs number (NCBI) 
    CHR_POS: Chromosomal position associated with rs number (dbSNP Build 132, NCBI) 
    REPORTED GENE (S): Gene(s) reported by author 
    MAPPED GENE(S): Gene(s) mapped to the strongest SNP (NCBI). If the SNP is located 
        within a gene, that gene is listed. If the SNP is intergenic, the upstream and 
        downstream genes are listed, separated by a hyphen. UPSTREAM_GENE_ID: 
        Entrez Gene ID for nearest upstream gene to rs number, if not within gene 
        (NCBI) 
    DOWNSTREAM_GENE_ID: Entrez Gene ID for nearest downstream gene to rs 
        number, if not within gene (NCBI) 
    SNP_GENE_IDS: Entrez Gene ID, if rs number within gene; multiple genes denotes 
        overlapping transcripts (NCBI) 
    UPSTREAM_GENE_DISTANCE: distance in kb for nearest upstream gene to rs 
        number, if not within gene (NCBI) 
    DOWNSTREAM_GENE_DISTANCE: distance in kb for nearest downstream gene to rs 
        number, if not within gene (NCBI) 
    STRONGEST SNP-RISK ALLELE: SNP(s) most strongly associated with trait + risk 
        allele (? for unknown risk allele). May also refer to a haplotype. 
    SNPS: Strongest SNP; if a haplotype is reported above, may include more than one rs 
        number (multiple SNPs comprising the haplotype) 
    MERGED: denotes whether the SNP has been merged into a subsequent rs record (0 = 
        no; 1 = yes; NCBI) SNP_ID_CURRENT: current rs number (will differ from strongest 
        SNP when merged =1) 
    CONTEXT: SNP functional class (NCBI) 
    INTERGENIC: denotes whether SNP is in intergenic region (1 = no; 2 = yes; NCBI) 
    RISK ALLELE FREQUENCY: Reported risk allele frequency associated with strongest 
    SNP 
    P-VALUE: Reported p-value for strongest SNP risk allele (linked to dbGaP Association 
        Browser) 
    PVALUE_MLOG: -log(p-value) P-VALUE (TEXT): Information describing context of p-value (e.g. females, smokers). 
        Note that p-values are rounded to 1 significant digit (for example, a published 
        p-value of 4.8 x 10-7 is rounded to 5 x 10-7). 
    OR or BETA: Reported odds ratio or beta-coefficient associated with strongest SNP risk 
    Allele 95% CI (TEXT): Reported 95% confidence interval associated with strongest SNP 
        risk allele 
    PLATFORM (SNPS PASSING QC): Genotyping platform manufacturer used in Stage 1; 
        also includes notation of pooled DNA study design or imputation of SNPs, where 
        applicable 
    CNV: Study of copy number variation (yes/no)
    """
    # 3
    date = db.DateProperty(required=True) 
    # 1
    pubmed = db.IntegerProperty()
    # 2
    author = db.StringProperty()
    # 5
    link = db.LinkProperty(required=True)
    # 4
    journal = db.StringProperty()
    # 6
    study = db.StringProperty()
    # 7
    disease = db.StringProperty()
    # 8
    sample_size = db.StringProperty()
    # 9
    replicate_size = db.StringProperty()
    # 10
    region = db.StringProperty()
    # 12
    chr_position = db.IntegerProperty()
    # 13
    r_gene = db.StringProperty() # reported gene
    # mapped gene: 14
    m_gene = db.StringProperty()
    # 18
    upstream_gene = db.StringProperty()
    # 19
    downstream_gene = db.StringProperty()
    # 20
    snp_allele = db.StringProperty()
    # 21
    snps = db.StringListProperty()
    # 23
    snpid = db.IntegerProperty()
    # 24
    context = db.StringProperty()
    # 25
    intergenic = db.IntegerProperty()
    # 26
    riscAlleleFrequency = db.FloatProperty()
    # 27
    p_value = db.FloatProperty()
    # 30
    OR_beta = db.FloatProperty()
    # 31
    CI95 = db.StringProperty()
    # 32
    Platform = db.StringProperty()