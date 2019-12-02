# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    ctyid = models.AutoField(db_column='ctyId', primary_key=True)  # Field name made lowercase.
    ctyname = models.CharField(db_column='ctyName', unique=True, max_length=20)  # Field name made lowercase.
    ctystate = models.CharField(db_column='ctyState', max_length=2)  # Field name made lowercase.
    ctyzipcode = models.CharField(db_column='ctyZipcode', max_length=5)  # Field name made lowercase.
    ctypopulation = models.IntegerField(db_column='ctyPopulation', blank=True, null=True)  # Field name made lowercase.
    ctycrimerate = models.DecimalField(db_column='ctyCrimeRate', max_digits=7, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.ctyname

    class Meta:
        managed = True
        db_table = 'City'


class Community(models.Model):
    cmtid = models.AutoField(db_column='cmtId', primary_key=True)  # Field name made lowercase.
    sttid = models.ForeignKey('Street', models.DO_NOTHING, db_column='sttId')  # Field name made lowercase.
    cmtname = models.CharField(db_column='cmtName', max_length=64)  # Field name made lowercase.
    cmtlatitude = models.DecimalField(db_column='cmtLatitude', max_digits=10, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    cmtlongitude = models.DecimalField(db_column='cmtLongitude', max_digits=10, decimal_places=7, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.cmtname

    class Meta:
        managed = True
        db_table = 'Community'


class Googleuser(models.Model):
    usrid = models.AutoField(db_column='usrId', primary_key=True)  # Field name made lowercase.
    usrname = models.CharField(db_column='usrName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.usrname

    class Meta:
        managed = True
        db_table = 'GoogleUser'


class Grocery(models.Model):
    grcid = models.AutoField(db_column='grcId', primary_key=True)  # Field name made lowercase.
    sttid = models.ForeignKey('Street', models.DO_NOTHING, db_column='sttId')  # Field name made lowercase.
    grcdescription = models.CharField(db_column='grcDescription', max_length=30, blank=True, null=True)  # Field name made lowercase.
    grctype = models.SmallIntegerField(db_column='grcType', blank=True, null=True)  # Field name made lowercase.
    grclatitude = models.DecimalField(db_column='grcLatitude', max_digits=10, decimal_places=7, blank=True, null=True)  # Field name made lowercase.
    grclongitude = models.DecimalField(db_column='grcLongitude', max_digits=10, decimal_places=7, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.grcdescription

    class Meta:
        managed = True
        db_table = 'Grocery'


class Residence(models.Model):
    rsdid = models.AutoField(db_column='rsdId', primary_key=True)  # Field name made lowercase.
    cmtid = models.ForeignKey(Community, models.DO_NOTHING, db_column='cmtId')  # Field name made lowercase.
    rsddescription = models.CharField(db_column='rsdDescription', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rsdsqft = models.IntegerField(db_column='rsdSqFt', blank=True, null=True)  # Field name made lowercase.
    rsdbedroom = models.SmallIntegerField(db_column='rsdBedroom', blank=True, null=True)  # Field name made lowercase.
    rsdbathroom = models.SmallIntegerField(db_column='rsdBathroom', blank=True, null=True)  # Field name made lowercase.
    rsdprice = models.DecimalField(db_column='rsdPrice', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rsdtype = models.CharField(db_column='rsdType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rsdyearbuilt = models.IntegerField(db_column='rsdYearBuilt', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.rsdid)

    class Meta:
        managed = True
        db_table = 'Residence'


class Review(models.Model):
    rvwid = models.AutoField(db_column='rvwId', primary_key=True)  # Field name made lowercase.
    usrid = models.ForeignKey(Googleuser, models.DO_NOTHING, db_column='usrId')  # Field name made lowercase.
    cmtid = models.ForeignKey(Community, models.DO_NOTHING, db_column='cmtId')  # Field name made lowercase.
    rvwdate = models.DateTimeField(db_column='rvwDate', blank=True, null=True)  # Field name made lowercase.
    rvwrate = models.SmallIntegerField(db_column='rvwRate', blank=True, null=True)  # Field name made lowercase.
    rvwdescription = models.CharField(db_column='rvwDescription', max_length=4096, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.rvwid)

    class Meta:
        managed = True
        db_table = 'Review'


class Stop(models.Model):
    stpid = models.AutoField(db_column='stpId', primary_key=True)  # Field name made lowercase.
    trnid = models.ForeignKey('Transportation', models.DO_NOTHING, db_column='trnId')  # Field name made lowercase.
    cmtid = models.ForeignKey(Community, models.DO_NOTHING, db_column='cmtId')  # Field name made lowercase.

    def __str__(self):
        return str(self.stpid)

    class Meta:
        managed = True
        db_table = 'Stop'
        unique_together = (('stpid', 'trnid', 'cmtid'),)


class Street(models.Model):
    sttid = models.AutoField(db_column='sttId', primary_key=True)  # Field name made lowercase.
    ctyid = models.ForeignKey(City, models.DO_NOTHING, db_column='ctyId')  # Field name made lowercase.
    sttname = models.CharField(db_column='sttName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.sttname

    class Meta:
        managed = True
        db_table = 'Street'


class Transportation(models.Model):
    trnid = models.AutoField(db_column='trnId', primary_key=True)  # Field name made lowercase.
    trndescription = models.CharField(db_column='trnDescription', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.trndescription

    class Meta:
        managed = True
        db_table = 'Transportation'

