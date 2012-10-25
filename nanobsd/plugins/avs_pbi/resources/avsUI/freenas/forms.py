import os
import platform
import pwd

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from avsUI.freenas import models, utils


class AVSForm(forms.ModelForm):

    class Meta:
        model = models.AVS
        #widgets = {
        #    'admin_pw': forms.widgets.PasswordInput(),
        #}
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail = kwargs.pop('jail')
        super(AVSForm, self).__init__(*args, **kwargs)

        #if self.instance.admin_pw:
        #    self.fields['admin_pw'].required = False

    def save(self, *args, **kwargs):
        obj = super(AVSForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.avs_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('avs_enable="YES"\n')

            #avs_flags = ""
            #for value in advanced_settings.values():
            #    avs_flags += value + " "
            #f.write('avs_flags="%s"\n' % (avs_flags, ))

        os.system(os.path.join(utils.avs_pbi_path, "tweak-rcconf"))
