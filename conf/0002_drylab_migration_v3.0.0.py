# Generated by Django 3.2 on 2023-04-29 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("drylab", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceState",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("state_value", models.CharField(max_length=50)),
                (
                    "state_display",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("show_in_stats", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "drylab_service_state",
            },
        ),
        migrations.RenameField(
            model_name="availableservice",
            old_name="availServiceDescription",
            new_name="avail_service_description",
        ),
        migrations.RenameField(
            model_name="availableservice",
            old_name="serviceId",
            new_name="service_id",
        ),
        migrations.RenameField(
            model_name="availableservice",
            old_name="inUse",
            new_name="service_in_use",
        ),
        migrations.RenameField(
            model_name="configsetting",
            old_name="configurationValue",
            new_name="configuration_value",
        ),
        migrations.RenameField(
            model_name="delivery",
            old_name="deliveryDate",
            new_name="delivery_date",
        ),
        migrations.RenameField(
            model_name="delivery",
            old_name="deliveryNotes",
            new_name="delivery_notes",
        ),
        migrations.RenameField(
            model_name="delivery",
            old_name="executionEndDate",
            new_name="execution_end_date",
        ),
        migrations.RenameField(
            model_name="delivery",
            old_name="executionStartDate",
            new_name="execution_start_date",
        ),
        migrations.RenameField(
            model_name="delivery",
            old_name="executionTime",
            new_name="execution_time",
        ),
        migrations.RenameField(
            model_name="delivery",
            old_name="permanentUsedSpace",
            new_name="permanent_used_space",
        ),
        migrations.RenameField(
            model_name="delivery",
            old_name="pipelinesInDelivery",
            new_name="pipelines_in_delivery",
        ),
        migrations.RenameField(
            model_name="delivery",
            old_name="temporaryUsedSpace",
            new_name="temporary_used_space",
        ),
        migrations.RenameField(
            model_name="parameterpipeline",
            old_name="parameterName",
            new_name="parameter_name",
        ),
        migrations.RenameField(
            model_name="parameterpipeline",
            old_name="parameterPipeline",
            new_name="parameter_pipeline",
        ),
        migrations.RenameField(
            model_name="parameterpipeline",
            old_name="parameterType",
            new_name="parameter_type",
        ),
        migrations.RenameField(
            model_name="parameterpipeline",
            old_name="parameterValue",
            new_name="parameter_value",
        ),
        migrations.RenameField(
            model_name="pipelines",
            old_name="pipelineDescription",
            new_name="pipeline_description",
        ),
        migrations.RenameField(
            model_name="pipelines",
            old_name="pipelineFile",
            new_name="pipeline_file",
        ),
        migrations.RenameField(
            model_name="pipelines",
            old_name="pipelineInUse",
            new_name="pipeline_in_use",
        ),
        migrations.RenameField(
            model_name="pipelines",
            old_name="pipelineName",
            new_name="pipeline_name",
        ),
        migrations.RenameField(
            model_name="pipelines",
            old_name="pipelineUrl",
            new_name="pipeline_url",
        ),
        migrations.RenameField(
            model_name="pipelines",
            old_name="pipelineVersion",
            new_name="pipeline_version",
        ),
        migrations.RenameField(
            model_name="pipelines",
            old_name="userName",
            new_name="user_name",
        ),
        migrations.RenameField(
            model_name="requestedsamplesinservices",
            old_name="onlyRecordedSample",
            new_name="only_recorded_sample",
        ),
        migrations.RenameField(
            model_name="requestedsamplesinservices",
            old_name="projectKey",
            new_name="project_key",
        ),
        migrations.RenameField(
            model_name="requestedsamplesinservices",
            old_name="projectName",
            new_name="project_name",
        ),
        migrations.RenameField(
            model_name="requestedsamplesinservices",
            old_name="runName",
            new_name="run_name",
        ),
        migrations.RenameField(
            model_name="requestedsamplesinservices",
            old_name="runNameKey",
            new_name="run_name_key",
        ),
        migrations.RenameField(
            model_name="requestedsamplesinservices",
            old_name="sampleKey",
            new_name="sample_key",
        ),
        migrations.RenameField(
            model_name="requestedsamplesinservices",
            old_name="sampleName",
            new_name="sample_name",
        ),
        migrations.RenameField(
            model_name="requestedsamplesinservices",
            old_name="samplePath",
            new_name="sample_path",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="availableServices",
            new_name="available_services",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionAsignedUser",
            new_name="resolution_assigned_user",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionDate",
            new_name="resolution_date",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionDeliveryDate",
            new_name="resolution_delivery_date",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionEstimatedDate",
            new_name="resolution_estimated_date",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionFullNumber",
            new_name="resolution_full_number",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionOnInProgressDate",
            new_name="resolution_in_progress_date",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionNotes",
            new_name="resolution_notes",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionNumber",
            new_name="resolution_number",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionPdfFile",
            new_name="resolution_pdf_file",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionPipelines",
            new_name="resolution_pipelines",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionOnQueuedDate",
            new_name="resolution_queued_date",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionState",
            new_name="resolution_state",
        ),
        migrations.RenameField(
            model_name="resolutionparameters",
            old_name="resolutionParamNotes",
            new_name="resolution_param_notes",
        ),
        migrations.RenameField(
            model_name="resolutionparameters",
            old_name="resolutionParamValue",
            new_name="resolution_param_value",
        ),
        migrations.RenameField(
            model_name="resolutionparameters",
            old_name="resolutionParameter",
            new_name="resolution_parameter",
        ),
        migrations.RenameField(
            model_name="resolutionstates",
            old_name="resolutionStateName",
            new_name="state_value",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceOnApprovedDate",
            new_name="service_approved_date",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceAvailableService",
            new_name="service_available_service",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceCreatedOnDate",
            new_name="service_created_date",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceOnDeliveredDate",
            new_name="service_delivered_date",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceNotes",
            new_name="service_notes",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceProjectNames",
            new_name="service_project_names",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceOnRejectedDate",
            new_name="service_rejected_date",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceRequestInt",
            new_name="service_request_int",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceRequestNumber",
            new_name="service_request_number",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceRunSpecs",
            new_name="service_run_specs",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceSeqCenter",
            new_name="service_center",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceSequencingPlatform",
            new_name="service_sequencing_platform",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceUserId",
            new_name="service_user_id",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="serviceStatus",
            new_name="service_status",
        ),
        migrations.RenameField(
            model_name="uploadservicefile",
            old_name="uploadFile",
            new_name="upload_file",
        ),
        migrations.RenameField(
            model_name="uploadservicefile",
            old_name="uploadFileName",
            new_name="upload_file_name",
        ),
        migrations.RenameField(
            model_name="uploadservicefile",
            old_name="uploadService",
            new_name="upload_service",
        ),
        migrations.RenameField(
            model_name="configsetting",
            old_name="configurationName",
            new_name="configuration_name",
        ),
        migrations.RenameField(
            model_name="delivery",
            old_name="deliveryResolutionID",
            new_name="delivery_resolution_id",
        ),
        migrations.RenameField(
            model_name="requestedsamplesinservices",
            old_name="samplesInService",
            new_name="samples_in_service",
        ),
        migrations.RenameField(
            model_name="resolution",
            old_name="resolutionServiceID",
            new_name="resolution_service_id",
        ),
        migrations.RemoveField(
            model_name="service",
            name="serviceFileExt",
        ),
        migrations.RemoveField(
            model_name="delivery",
            name="delivery_date",
        ),
        migrations.AlterField(
            model_name="configsetting",
            name="configuration_name",
            field=models.CharField(default=None, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="delivery",
            name="delivery_resolution_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="delivery",
                to="drylab.resolution",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="requestedsamplesinservices",
            name="samples_in_service",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="samples",
                to="drylab.service",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="resolution",
            name="resolution_service_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="resolutions",
                to="drylab.service",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="resolutionstates",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="resolutionstates",
            name="state_display",
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name="service",
            name="service_status",
            field=models.CharField(
                choices=[
                    ("recorded", "Recorded"),
                    ("approved", "Approved"),
                    ("rejected", "Rejected"),
                    ("queued", "Queued"),
                    ("in_progress", "In Progress"),
                    ("delivered", "Delivered"),
                    ("archived", "Archived"),
                ],
                max_length=15,
                verbose_name="Service status",
            ),
        ),
        migrations.AlterField(
            model_name="resolution",
            name="resolution_number",
            field=models.CharField(
                max_length=255, null=True, verbose_name="Resolution name"
            ),
        ),
        migrations.AlterField(
            model_name="uploadservicefile",
            name="upload_file",
            field=models.FileField(upload_to="drylab/service_files"),
        ),
        migrations.AlterModelTable(
            name="availableservice",
            table="drylab_available_service",
        ),
        migrations.AlterModelTable(
            name="configsetting",
            table="drylab_config_setting",
        ),
        migrations.AlterModelTable(
            name="delivery",
            table="drylab_delivery",
        ),
        migrations.AlterModelTable(
            name="parameterpipeline",
            table="drylab_parameter_pipeline",
        ),
        migrations.AlterModelTable(
            name="pipelines",
            table="drylab_pipelines",
        ),
        migrations.AlterModelTable(
            name="requestedsamplesinservices",
            table="drylab_request_samples_in_services",
        ),
        migrations.AlterModelTable(
            name="resolution",
            table="drylab_resolution",
        ),
        migrations.AlterModelTable(
            name="resolutionparameters",
            table="drylab_resolution_parameters",
        ),
        migrations.AlterModelTable(
            name="resolutionstates",
            table="drylab_resolution_states",
        ),
        migrations.AlterModelTable(
            name="service",
            table="drylab_service",
        ),
        migrations.AlterModelTable(
            name="uploadservicefile",
            table="drylab_upload_service_file",
        ),
        migrations.DeleteModel(
            name="FileExt",
        ),
        migrations.AddField(
            model_name="service",
            name="service_state",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="drylab.servicestate",
                verbose_name="Service State",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="service_request_number",
            field=models.CharField(max_length=80, null=True, verbose_name="Service ID"),
        ),
    ]
