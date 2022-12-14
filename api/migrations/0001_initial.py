# Generated by Django 4.1.3 on 2023-01-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddSetName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_add_set_name',
            },
        ),
        migrations.CreateModel(
            name='AdSetBidStrategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_ad_set_bid_strategy',
            },
        ),
        migrations.CreateModel(
            name='AdSetRunStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_ad_set_run_status',
            },
        ),
        migrations.CreateModel(
            name='AdStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_ad_status',
            },
        ),
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='AudienceNetworkPositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_audience_network_positions',
            },
        ),
        migrations.CreateModel(
            name='BillingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_billing_event',
            },
        ),
        migrations.CreateModel(
            name='BuyingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_buying_type',
            },
        ),
        migrations.CreateModel(
            name='CampaignBidStrategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_campaign_bid_strategy',
            },
        ),
        migrations.CreateModel(
            name='CampaignName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_campaign_name',
            },
        ),
        migrations.CreateModel(
            name='CampaignObjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_campaign_objective',
            },
        ),
        migrations.CreateModel(
            name='CampaignStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_campaign_status',
            },
        ),
        migrations.CreateModel(
            name='Campiagn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('platform', models.CharField(max_length=120)),
                ('placement', models.CharField(max_length=120)),
                ('page_name', models.CharField(max_length=120)),
                ('campaign_name', models.CharField(max_length=150)),
                ('campaign_objective', models.CharField(max_length=120)),
                ('retargeting', models.CharField(blank=True, max_length=120, null=True)),
                ('engagement', models.CharField(blank=True, max_length=120, null=True)),
                ('add_set_name', models.CharField(max_length=120)),
                ('audience', models.CharField(blank=True, max_length=120, null=True)),
                ('excluded_custom', models.CharField(blank=True, max_length=120, null=True)),
                ('add_name', models.CharField(max_length=120)),
                ('audience_interest', models.CharField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('body', models.CharField(blank=True, max_length=300, null=True)),
                ('link_description', models.CharField(blank=True, max_length=250, null=True)),
                ('image_video_file_name', models.CharField(blank=True, max_length=120, null=True)),
                ('display_link', models.CharField(blank=True, max_length=250, null=True)),
                ('product_1_link', models.CharField(blank=True, max_length=250, null=True)),
                ('product_name', models.CharField(blank=True, max_length=120, null=True)),
                ('product_image_hash', models.CharField(blank=True, max_length=120, null=True)),
                ('call_to_action', models.CharField(blank=True, max_length=120, null=True)),
                ('store_id', models.CharField(blank=True, max_length=120, null=True)),
                ('approval_name', models.CharField(blank=True, max_length=120, null=True)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='ExcludedCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_excluded_custom',
            },
        ),
        migrations.CreateModel(
            name='FacebookPositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_facebook_positions',
            },
        ),
        migrations.CreateModel(
            name='InstagramPositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_instagram_positions',
            },
        ),
        migrations.CreateModel(
            name='MessengerPositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_messenger_positions',
            },
        ),
        migrations.CreateModel(
            name='OculusPositions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_oculus_positions',
            },
        ),
        migrations.CreateModel(
            name='OptimizationGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_optimization_goal',
            },
        ),
        migrations.CreateModel(
            name='PageName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'api_page_name',
            },
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Retargeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=140)),
            ],
        ),
    ]
