from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import traineeproject_schedule

traineeproject_visit_schedule = VisitSchedule(

    name='traineeproject_visit_schedule',
    verbose_name='traineeproject',
    offstudy_model='traineeproject_prn.subjectoffstudy',
    locator_model= 'traineeproject_subject.personalcontactinfo',
    death_report_model='traineeproject_prn.deathreport',
    previous_visit_schedule=None)

traineeproject_visit_schedule.add_schedule(traineeproject_schedule)
site_visit_schedules.register(traineeproject_visit_schedule)