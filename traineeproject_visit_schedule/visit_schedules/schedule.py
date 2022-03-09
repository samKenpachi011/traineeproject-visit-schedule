from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from .crfs import crf, trainee_crfs_prn
from .requisions import requisitions
from ..constants import DAY1, DAY7, DAY14

class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=trainee_crfs_prn or crfs_prn,
            requisitions_prn=requisitions_prn,
            **kwargs)

traineeproject_schedule = Schedule(
    name='schedule',
    verbose_name='Trainee Project Schedule Day 1 to Day3',
    onschedule_model='traineeproject_subject.onschedule',
    offschedule_model='traineeproject_subject.offschedule',
    consent_model='traineeproject_subject.subjectconsent',
    appointment_model='edc_appointment.appointment',

)

visit0 = Visit(
    code=DAY1,
    title='Day0',
    timepoint=1,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    cfrs=crf.get('initial'),
    facility_name='5-day clinic'
)
visit1 = Visit(
    code=DAY7,
    title='Day7',
    timepoint=2,
    rbase=relativedelta(days=7),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=requisitions,
    cfrs=crf.get('visit_2'),
    facility_name='5-day clinic'
)
visit2 = Visit(
    code=DAY14,
    title='Day14',
    timepoint=3,
    rbase=relativedelta(days=14),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=requisitions,
    cfrs=crf.get('visit_3'),
    facility_name='5-day clinic'
)

traineeproject_schedule.add_visit(visit=visit0)
traineeproject_schedule.add_visit(visit=visit1)
traineeproject_schedule.add_visit(visit=visit2)
