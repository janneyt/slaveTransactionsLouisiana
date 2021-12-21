# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Products(models.Model):
    product_name = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'products'


class Slavetransactions(models.Model):
    index = models.IntegerField(primary_key=True, blank=True, null=False)
    docdate = models.TextField(db_column='DOCDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    year = models.TextField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    docno = models.TextField(db_column='DOCNO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    notary = models.TextField(db_column='NOTARY', blank=True, null=True)  # Field name made lowercase.
    coder = models.FloatField(db_column='CODER', blank=True, null=True)  # Field name made lowercase.
    dateinv = models.TextField(db_column='DATEINV', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    datesale = models.TextField(db_column='DATESALE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    depot = models.FloatField(db_column='DEPOT', blank=True, null=True)  # Field name made lowercase.
    parish = models.TextField(db_column='PARISH', blank=True, null=True)  # Field name made lowercase.
    location = models.FloatField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    doctype = models.IntegerField(db_column='DOCTYPE', blank=True, null=True)  # Field name made lowercase.
    revolts = models.FloatField(db_column='REVOLTS', blank=True, null=True)  # Field name made lowercase.
    maroon = models.FloatField(db_column='MAROON', blank=True, null=True)  # Field name made lowercase.
    language = models.IntegerField(db_column='LANGUAGE', blank=True, null=True)  # Field name made lowercase.
    linguistic = models.FloatField(db_column='LINGUISTIC', blank=True, null=True)  # Field name made lowercase.
    estfree = models.FloatField(db_column='ESTFREE', blank=True, null=True)  # Field name made lowercase.
    free = models.FloatField(db_column='FREE', blank=True, null=True)  # Field name made lowercase.
    estate_of = models.TextField(db_column='ESTATE_OF', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FIRSTNAME', blank=True, null=True)  # Field name made lowercase.
    estate = models.TextField(db_column='ESTATE', blank=True, null=True)  # Field name made lowercase.
    estatepop = models.FloatField(db_column='ESTATEPOP', blank=True, null=True)  # Field name made lowercase.
    seller = models.TextField(db_column='SELLER', blank=True, null=True)  # Field name made lowercase.
    first1 = models.TextField(db_column='FIRST1', blank=True, null=True)  # Field name made lowercase.
    buyer = models.TextField(db_column='BUYER', blank=True, null=True)  # Field name made lowercase.
    first2 = models.TextField(db_column='FIRST2', blank=True, null=True)  # Field name made lowercase.
    went = models.FloatField(db_column='WENT', blank=True, null=True)  # Field name made lowercase.
    namexplain = models.TextField(db_column='NAMEXPLAIN', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    nametype = models.IntegerField(db_column='NAMETYPE', blank=True, null=True)  # Field name made lowercase.
    islamic = models.FloatField(db_column='ISLAMIC', blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='SEX', blank=True, null=True)  # Field name made lowercase.
    race = models.FloatField(db_column='RACE', blank=True, null=True)  # Field name made lowercase.
    age = models.FloatField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    agecatn = models.FloatField(db_column='AGECATN', blank=True, null=True)  # Field name made lowercase.
    skills = models.TextField(db_column='SKILLS', blank=True, null=True)  # Field name made lowercase.
    skillcat = models.FloatField(db_column='SKILLCAT', blank=True, null=True)  # Field name made lowercase.
    expert = models.FloatField(db_column='EXPERT', blank=True, null=True)  # Field name made lowercase.
    apprentice = models.FloatField(db_column='APPRENTICE', blank=True, null=True)  # Field name made lowercase.
    alittle = models.FloatField(db_column='ALITTLE', blank=True, null=True)  # Field name made lowercase.
    skill2 = models.FloatField(db_column='SKILL2', blank=True, null=True)  # Field name made lowercase.
    skill3 = models.FloatField(db_column='SKILL3', blank=True, null=True)  # Field name made lowercase.
    skill4 = models.FloatField(db_column='SKILL4', blank=True, null=True)  # Field name made lowercase.
    skill5 = models.FloatField(db_column='SKILL5', blank=True, null=True)  # Field name made lowercase.
    character = models.TextField(db_column='CHARACTER', blank=True, null=True)  # Field name made lowercase.
    charcat = models.FloatField(db_column='CHARCAT', blank=True, null=True)  # Field name made lowercase.
    charcat2 = models.FloatField(db_column='CHARCAT2', blank=True, null=True)  # Field name made lowercase.
    charcat3 = models.FloatField(db_column='CHARCAT3', blank=True, null=True)  # Field name made lowercase.
    sick = models.TextField(db_column='SICK', blank=True, null=True)  # Field name made lowercase.
    sickcat = models.FloatField(db_column='SICKCAT', blank=True, null=True)  # Field name made lowercase.
    sick2 = models.FloatField(db_column='SICK2', blank=True, null=True)  # Field name made lowercase.
    sick3 = models.FloatField(db_column='SICK3', blank=True, null=True)  # Field name made lowercase.
    sick4 = models.FloatField(db_column='SICK4', blank=True, null=True)  # Field name made lowercase.
    spell = models.TextField(db_column='SPELL', blank=True, null=True)  # Field name made lowercase.
    birthpl = models.FloatField(db_column='BIRTHPL', blank=True, null=True)  # Field name made lowercase.
    aflang = models.FloatField(db_column='AFLANG', blank=True, null=True)  # Field name made lowercase.
    brut = models.FloatField(db_column='BRUT', blank=True, null=True)  # Field name made lowercase.
    group = models.FloatField(db_column='GROUP', blank=True, null=True)  # Field name made lowercase.
    groupmemb = models.TextField(db_column='GROUPMEMB', blank=True, null=True)  # Field name made lowercase.
    invcur = models.TextField(db_column='INVCUR', blank=True, null=True)  # Field name made lowercase.
    invvalue = models.FloatField(db_column='INVVALUE', blank=True, null=True)  # Field name made lowercase.
    invvalp = models.FloatField(db_column='INVVALP', blank=True, null=True)  # Field name made lowercase.
    salecur = models.TextField(db_column='SALECUR', blank=True, null=True)  # Field name made lowercase.
    salevalue = models.FloatField(db_column='SALEVALUE', blank=True, null=True)  # Field name made lowercase.
    salevalp = models.FloatField(db_column='SALEVALP', blank=True, null=True)  # Field name made lowercase.
    family_y_n = models.FloatField(db_column='FAMILY_Y_N', blank=True, null=True)  # Field name made lowercase.
    family = models.TextField(db_column='FAMILY', blank=True, null=True)  # Field name made lowercase.
    children = models.FloatField(db_column='CHILDREN', blank=True, null=True)  # Field name made lowercase.
    male = models.FloatField(db_column='MALE', blank=True, null=True)  # Field name made lowercase.
    female = models.FloatField(db_column='FEMALE', blank=True, null=True)  # Field name made lowercase.
    under5 = models.FloatField(db_column='UNDER5', blank=True, null=True)  # Field name made lowercase.
    pregnant = models.FloatField(db_column='PREGNANT', blank=True, null=True)  # Field name made lowercase.
    mother = models.FloatField(db_column='MOTHER', blank=True, null=True)  # Field name made lowercase.
    agemom = models.FloatField(db_column='AGEMOM', blank=True, null=True)  # Field name made lowercase.
    racemom = models.FloatField(db_column='RACEMOM', blank=True, null=True)  # Field name made lowercase.
    invwmom = models.FloatField(db_column='INVWMOM', blank=True, null=True)  # Field name made lowercase.
    soldwmom = models.FloatField(db_column='SOLDWMOM', blank=True, null=True)  # Field name made lowercase.
    spnatmom = models.TextField(db_column='SPNATMOM', blank=True, null=True)  # Field name made lowercase.
    ormom = models.FloatField(db_column='ORMOM', blank=True, null=True)  # Field name made lowercase.
    mate = models.FloatField(db_column='MATE', blank=True, null=True)  # Field name made lowercase.
    matename = models.TextField(db_column='MATENAME', blank=True, null=True)  # Field name made lowercase.
    agemate = models.FloatField(db_column='AGEMATE', blank=True, null=True)  # Field name made lowercase.
    agecatmate = models.FloatField(db_column='AGECATMATE', blank=True, null=True)  # Field name made lowercase.
    racemate = models.FloatField(db_column='RACEMATE', blank=True, null=True)  # Field name made lowercase.
    spelnamate = models.TextField(db_column='SPELNAMATE', blank=True, null=True)  # Field name made lowercase.
    originmate = models.FloatField(db_column='ORIGINMATE', blank=True, null=True)  # Field name made lowercase.
    father = models.FloatField(db_column='FATHER', blank=True, null=True)  # Field name made lowercase.
    agedad = models.FloatField(db_column='AGEDAD', blank=True, null=True)  # Field name made lowercase.
    racedad = models.FloatField(db_column='RACEDAD', blank=True, null=True)  # Field name made lowercase.
    spnadad = models.TextField(db_column='SPNADAD', blank=True, null=True)  # Field name made lowercase.
    ordad = models.FloatField(db_column='ORDAD', blank=True, null=True)  # Field name made lowercase.
    grandchild = models.FloatField(db_column='GRANDCHILD', blank=True, null=True)  # Field name made lowercase.
    grandsons = models.FloatField(db_column='GRANDSONS', blank=True, null=True)  # Field name made lowercase.
    gdaughters = models.FloatField(db_column='GDAUGHTERS', blank=True, null=True)  # Field name made lowercase.
    grandma = models.FloatField(db_column='GRANDMA', blank=True, null=True)  # Field name made lowercase.
    agegrandma = models.FloatField(db_column='AGEGRANDMA', blank=True, null=True)  # Field name made lowercase.
    spnagm = models.TextField(db_column='SPNAGM', blank=True, null=True)  # Field name made lowercase.
    orgrandma = models.FloatField(db_column='ORGRANDMA', blank=True, null=True)  # Field name made lowercase.
    granpa = models.FloatField(db_column='GRANPA', blank=True, null=True)  # Field name made lowercase.
    agegrandpa = models.FloatField(db_column='AGEGRANDPA', blank=True, null=True)  # Field name made lowercase.
    spnagrpa = models.TextField(db_column='SPNAGRPA', blank=True, null=True)  # Field name made lowercase.
    orgrandpa = models.FloatField(db_column='ORGRANDPA', blank=True, null=True)  # Field name made lowercase.
    emancip = models.FloatField(db_column='EMANCIP', blank=True, null=True)  # Field name made lowercase.
    dead = models.FloatField(db_column='DEAD', blank=True, null=True)  # Field name made lowercase.
    runaway = models.FloatField(db_column='RUNAWAY', blank=True, null=True)  # Field name made lowercase.
    enterprise = models.FloatField(db_column='ENTERPRISE', blank=True, null=True)  # Field name made lowercase.
    captain = models.TextField(db_column='CAPTAIN', blank=True, null=True)  # Field name made lowercase.
    slavetrade = models.TextField(db_column='SLAVETRADE', blank=True, null=True)  # Field name made lowercase.
    stport = models.FloatField(db_column='STPORT', blank=True, null=True)  # Field name made lowercase.
    ship = models.TextField(db_column='SHIP', blank=True, null=True)  # Field name made lowercase.
    arrivedate = models.TextField(db_column='ARRIVEDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    from_field = models.TextField(db_column='FROM', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    unbapt = models.TextField(db_column='UNBAPT', blank=True, null=True)  # Field name made lowercase.
    via = models.FloatField(db_column='VIA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slaveTransactions'
