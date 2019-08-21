from tastypie.resources import ModelResource
from API.models import *
from tastypie.authorization import Authorization

class ContaResource(ModelResource):
    class Meta:
        queryset = Conta.objects.all()
        include=['banco','money_in_account','number']
        authorization = Authorization()
        resource_name = 'account'
        allowed_methods=['patch','get']
        def __str__(self):
            return '%s %s %s' % (self.banco, self.money_in_account, self.number)

class GastosResource(ModelResource):
    class Meta:
        include=['date','price','descricao_gasto','number','id']
        queryset=Gastos.objects.all()
        authorization = Authorization()
        resource_name = 'expense'
        allowed_methods=['get','post']
        def __str__(self):
            return '%s %s' % (self.date, self.price)

class UsuarioResource(ModelResource):
    class Meta:
        include=['number', 'nome']
        allowed_methods=['get']
        queryset=Usuarios.objects.all()
        authorization = Authorization()
        resource_name = 'user'
        def __str__(self):
            return '%s %s %s %s' % (self.number, self.username, self.password, self.email)