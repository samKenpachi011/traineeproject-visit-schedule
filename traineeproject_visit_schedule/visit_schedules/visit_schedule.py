from edc_visit_schedule import VisitSchedule, site_visit_schedules
"""
 Visit schedule takes in
        name verbose_name previous_visit_schedule
        death_report_model offstudy_model locator_model
"""
traineeproject_visit_schedule = VisitSchedule(

    name='traineeproject_visit_schedule',
    verbose_name='Traineeproject',
    offstudy_model='',
    death_report_model='',
)
site_visit_schedules.register(traineeproject_visit_schedule)