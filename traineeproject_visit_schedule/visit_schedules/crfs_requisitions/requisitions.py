from edc_visit_schedule import FormsCollection, Requisition
from traineeproject_labs import sars_pcr_panel

requisitions = FormsCollection(
    Requisition(show_order=1, panel=sars_pcr_panel, required=False, additonal=False)
)
