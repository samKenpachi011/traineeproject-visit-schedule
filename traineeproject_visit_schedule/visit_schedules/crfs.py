from edc_visit_schedule import FormsCollection, Crf

crf = {}
"""
-To create form collections for crfs that are needed on certain visits
-create form group for prn :special forms that remind the user to fill them but not required
 --pass: demographics, education, engagement
-initial models to pass: demographics
-visit 2 : education
-visit 3 : community engagement

"""
trainee_crfs_prn = FormsCollection(
    Crf(show_order=1, model='traineeproject_subject.demographic'),
    Crf(show_order=2, model='traineeproject_subject.education'),
    Crf(show_order=3, model='traineeproject_subject.communityengagement'),
    name='trainee_crf_prn')


crfs_initial = FormsCollection(
    Crf(show_order=1, model='traineeproject_subject.demographic'),
    name='initial',)

crfs_visit_2 = FormsCollection(
    Crf(show_order=1, model='traineeproject_subject.education'),
    name='visit_2'
)

crfs_visit_3 = FormsCollection(
    Crf(show_order=1, model='traineeproject_subject.communityengagement'),
    name='visit_3'
)

crfs = {
    'initial':crfs_initial,
    'visit2':crfs_visit_2,
    'visit3':crfs_visit_3,
    'prn':trainee_crfs_prn}

# crf.update({
#     'initial':crfs_initial,
#     'visit2':crfs_visit_2,
#     'visit3':crfs_visit_3,
#     'prn':trainee_crfs_prn})

