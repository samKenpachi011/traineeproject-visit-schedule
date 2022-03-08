from edc_visit_schedule import VisitSchedule, site_visit_schedules
from .schedules import traineeproject_schedule
"""
 Visit schedule takes in
        name verbose_name previous_visit_schedule
        death_report_model offstudy_model locator_model
"""
# TODO:to update offstudy and death report
traineeproject_visit_schedule = VisitSchedule(

    name='traineeproject_visit_schedule',
    verbose_name='Traineeproject',
    offstudy_model='traineeproject_prn.subjectoffstudy',
    locator_model= 'traineeproject_subject.personalcontactinfo',
    death_report_model='traineeproject_prn.deathreport',
    previous_visit_schedule=None
)


traineeproject_visit_schedule.add_schedule(traineeproject_schedule)
site_visit_schedules.register(traineeproject_visit_schedule)