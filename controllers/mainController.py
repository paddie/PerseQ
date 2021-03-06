###
# Controller for main presentation
#
###
from Utilities import AppRequestHandler
from models.snp import snp

class snpSearch(AppRequestHandler):
    def get(self):
        snpids = snp.all()
        snpids.order("snpid")
        self.out({'snps':snpids})

class dashboard(AppRequestHandler):
    def get(self):
        self.out()

__routes__ = [('/',dashboard),
              ('/search/', snpSearch)]
