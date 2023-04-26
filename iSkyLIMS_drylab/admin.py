from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

import iSkyLIMS_drylab.models


class ResolutionStatesAdmin(admin.ModelAdmin):
    list_display = ["state_value"]


class ServiceStateAdmin(admin.ModelAdmin):
    list_display = ["state_value", "state_display", "description", "show_in_stats"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "service_request_number",
        "service_seq_center",
        "serviceUserId",
        "service_state",
        "service_created_date",
        "service_delivered_date",
    )
    list_filter = ["service_created_date"]
    search_fields = ["service_request_number__icontains"]


class RequestedSamplesInServicesAdmin(admin.ModelAdmin):
    list_display = ["samples_in_service", "sample_name", "project_name", "run_name"]


class UploadServiceFileAdmin(admin.ModelAdmin):
    list_display = ["upload_service", "upload_file", "upload_file_name"]
    search_fields = (
        "upload_service__service_request_number__icontains",
        "upload_file_name__icontains",
    )


class AvailableServiceAdmin(DjangoMpttAdmin):
    list_display = ["avail_service_description", "serviceId", "service_in_use"]


class ResolutionAdmin(admin.ModelAdmin):
    list_display = (
        "resolution_serviceID",
        "resolution_number",
        "resolution_state",
        "resolution_date",
        "resolution_estimated_date",
        "resolution_full_number",
        "resolution_asigned_user",
    )
    list_filter = ["resolution_date"]
    search_fields = [
        "resolutionNumber__icontains",
        "resolution_asigned_user__username__icontains",
    ]


class ResolutionParametersAdmin(admin.ModelAdmin):
    list_display = [
        "resolution",
        "resolution_parameter",
        "resolution_param_value",
        "resolution_param_notes",
    ]


class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        "delivery_resolutionID",
        "delivery_date",
        "execution_start_date",
        "execution_end_date",
        "execution_time",
        "permanent_used_space",
        "temporary_used_space",
        "delivery_notes",
    ]


class PipelinesManager(admin.ModelAdmin):
    list_display = [
        "pipeline_name",
        "pipeline_version",
        "pipeline_in_use",
        "pipeline_file",
    ]


class ParameterPipelineManager(admin.ModelAdmin):
    list_display = ["parameter_pipeline", "parameter_name", "parameter_value"]


class ConfigSettingAdmin(admin.ModelAdmin):
    list_display = ["configuration_name", "configuration_value"]


admin.site.register(iSkyLIMS_drylab.models.ServiceState, ServiceStateAdmin)
admin.site.register(iSkyLIMS_drylab.models.ResolutionStates, ResolutionStatesAdmin)
admin.site.register(iSkyLIMS_drylab.models.Service, ServiceAdmin)
admin.site.register(iSkyLIMS_drylab.models.UploadServiceFile, UploadServiceFileAdmin)
admin.site.register(iSkyLIMS_drylab.models.ResolutionParameters, ResolutionParametersAdmin)
admin.site.register(iSkyLIMS_drylab.models.RequestedSamplesInServices, RequestedSamplesInServicesAdmin)
admin.site.register(iSkyLIMS_drylab.models.AvailableService, AvailableServiceAdmin)
admin.site.register(iSkyLIMS_drylab.models.Resolution, ResolutionAdmin)
admin.site.register(iSkyLIMS_drylab.models.Delivery, DeliveryAdmin)
admin.site.register(iSkyLIMS_drylab.models.Pipelines, PipelinesManager)
admin.site.register(iSkyLIMS_drylab.models.ParameterPipeline, ParameterPipelineManager)
admin.site.register(iSkyLIMS_drylab.models.ConfigSetting, ConfigSettingAdmin)
