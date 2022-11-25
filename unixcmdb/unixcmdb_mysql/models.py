from django.db import models

# Create your models here.
class UnixLinuxActFull(models.Model):
    name = models.CharField(max_length=50)
    discovered_os_name = models.CharField(max_length=50, blank=True, null=True)
    host_osinstalltype = models.CharField(max_length=100, blank=True, null=True)
    environment = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    operation_location_limited_to = models.CharField(max_length=50, blank=True, null=True)
    externalstorage = models.CharField(db_column='ExternalStorage', max_length=10, blank=True, null=True)  # Field name made lowercase.
    os_description = models.CharField(max_length=50, blank=True, null=True)
    host_osrelease = models.CharField(max_length=20, blank=True, null=True)
    impact_classification = models.CharField(max_length=50, blank=True, null=True)
    time_zone = models.CharField(max_length=250, blank=True, null=True)
    housing_only = models.CharField(max_length=20, blank=True, null=True)
    backup = models.CharField(max_length=10, blank=True, null=True)
    time_server = models.CharField(max_length=200, blank=True, null=True)
    backup_environment = models.CharField(max_length=50, blank=True, null=True)
    patch_group = models.CharField(max_length=50, blank=True, null=True)
    asset_owner = models.CharField(max_length=50, blank=True, null=True)
    compliance_classification = models.CharField(max_length=50, blank=True, null=True)
    support_contract_identifier = models.CharField(max_length=50, blank=True, null=True)
    primary_dns_name = models.CharField(max_length=100, blank=True, null=True)
    password_owner = models.CharField(max_length=20, blank=True, null=True)
    discovered_model = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    reporting = models.CharField(max_length=20, blank=True, null=True)
    antivirus = models.CharField(max_length=10, blank=True, null=True)
    discovered_os_version = models.CharField(max_length=50, blank=True, null=True)
    last_discovery_time = models.CharField(max_length=20, blank=True, null=True)
    service_level_agreement = models.CharField(max_length=10, blank=True, null=True)
    assignment_group = models.CharField(max_length=50, blank=True, null=True)
    business_application = models.CharField(max_length=150, blank=True, null=True)
    customer = models.CharField(max_length=50, blank=True, null=True)
    calculated_location = models.CharField(max_length=250, blank=True, null=True)
    running_software = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unix_linux_act_full'

class UnixLinuxRetFull(models.Model):
    name = models.CharField(max_length=50)
    discovered_os_name = models.CharField(max_length=50, blank=True, null=True)
    host_osinstalltype = models.CharField(max_length=100, blank=True, null=True)
    environment = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    operation_location_limited_to = models.CharField(max_length=50, blank=True, null=True)
    externalstorage = models.CharField(db_column='ExternalStorage', max_length=10, blank=True, null=True)  # Field name made lowercase.
    os_description = models.CharField(max_length=50, blank=True, null=True)
    host_osrelease = models.CharField(max_length=20, blank=True, null=True)
    impact_classification = models.CharField(max_length=50, blank=True, null=True)
    time_zone = models.CharField(max_length=250, blank=True, null=True)
    housing_only = models.CharField(max_length=20, blank=True, null=True)
    backup = models.CharField(max_length=10, blank=True, null=True)
    time_server = models.CharField(max_length=200, blank=True, null=True)
    backup_environment = models.CharField(max_length=50, blank=True, null=True)
    patch_group = models.CharField(max_length=50, blank=True, null=True)
    asset_owner = models.CharField(max_length=50, blank=True, null=True)
    compliance_classification = models.CharField(max_length=50, blank=True, null=True)
    support_contract_identifier = models.CharField(max_length=50, blank=True, null=True)
    primary_dns_name = models.CharField(max_length=100, blank=True, null=True)
    password_owner = models.CharField(max_length=20, blank=True, null=True)
    discovered_model = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=200, blank=True, null=True)
    reporting = models.CharField(max_length=20, blank=True, null=True)
    antivirus = models.CharField(max_length=10, blank=True, null=True)
    discovered_os_version = models.CharField(max_length=50, blank=True, null=True)
    last_discovery_time = models.CharField(max_length=20, blank=True, null=True)
    service_level_agreement = models.CharField(max_length=10, blank=True, null=True)
    assignment_group = models.CharField(max_length=50, blank=True, null=True)
    business_application = models.CharField(max_length=150, blank=True, null=True)
    customer = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unix_linux_ret_full'

class ServerInOut(models.Model):
    name = models.TextField(blank=True, null=True)
    customer = models.TextField(blank=True, null=True)
    os_description = models.TextField(db_column='OS_Description', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(blank=True, null=True)
    change_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_in_out'

