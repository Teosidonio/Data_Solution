from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator

class Environments(models.Model):
    """ Defining our models for the Environment Page and information """
    STAGES = [
        ('DEVELOPMENT','DEVELOPMENT'),('SIT', 'SIT'), ('UAT','UAT'), ('STAGING/PRE-PROD','STAGING/PRE-PROD') , ('PRODUCTION','PRODUCTION')
    ]
    DATABASES = [
        ('POSTGRESQL','POSTGRESQL'), ('MariaDB','MariaDB'), ('MySQL','MySQL'), ('Oracle','Oracle'),
        ('MS SQL Server','MS SQL Server'),('SQLite3', 'SQLite3'), ('CosmosDB','CosmosDB'), ('MongoDB','MongoDB')
    ]

    PLATFORM = [
        ('MacOs','MacOs'), ('LINUX','LINUX'),
        ('WINDOWS','WINDOWS')
    ]
    HARDWARE = [
        ('PHISICAL_SERVER','PHISICAL_SERVER'), ('VIRTUAL MACHINE','VIRTUAL MACHINE'), ('CLOUD', 'CLOUD_AZURE')
    ]
    PROVIDER = [
        ('INTERNAL','INTERNAL'), ('OUTSOURCED','OUTSOURCED')
    ]
    STATUS = [
        ('LIVE','LIVE'), ('DOWN','DOWN')
    ]

    #env_id = models.AutoField(primary_key=True) models.DecimalField(max_digits=12, decimal_places=4, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=False)
    env_stage = models.CharField(max_length=100, choices=STAGES)
    platform = models.CharField(max_length=100, choices=PLATFORM)
    database = models.CharField(max_length=50, choices=DATABASES)
    run_stack = models.CharField(max_length=100)
    web_server = models.CharField(max_length=150)
    ip = models.CharField(max_length=15)
    hardware = models.CharField(max_length=50, choices=HARDWARE)
    product_app = models.CharField(max_length=200)
    provider = models.CharField(max_length=50, choices=PROVIDER)
    port = models.IntegerField()
    created_by = models.CharField(max_length=100)
    status = models.CharField(max_length=30, choices=STATUS)

    class Meta:
        ordering = ['date_created', 'name', 'env_stage', 'platform']

    def __str__(self):
        return f'{self.date_created} {self.name} {self.description} {self.env_stage} {self.platform} {self.database} {self.run_stack} {self.web_server} {self.ip} {self.hardware} {self.product_app} {self.port} {self.provider}  {self.created_by} {self.status}'

    def get_absolute_url(self):
        """ Gets absolute URL """
        return reverse('env-detail', kwargs={'pk': self.pk})



