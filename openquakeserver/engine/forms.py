from django import forms


class BaseForm(forms.Form):
    # Optional callback url to hit to start automatic migration of calculation
    # results once a calculation concludes
    job_config = forms.FileField(label='Job configuration (.ini file)')
    migration_callback_url = forms.URLField(
        required=False,
        label='URL to notify of calc completion',
    )
    owner_user = forms.CharField(
        required=False,
        label='Owner username of calculation results',
    )


class HazardForm(BaseForm):
    pass


class RiskForm(BaseForm):
    hazard_calc = forms.IntegerField(
        required=False,
        label='Hazard calculation ID',
    )
    hazard_result = forms.IntegerField(
        required=False,
        label='Hazard result ID',
    )
