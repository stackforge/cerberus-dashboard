#
#   Copyright (c) 2015 EUROGICIEL
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

from django.utils.translation import ugettext_lazy as _
import json

from horizon import tabs

from cerberusdashboard.security_reports import tables


class OverviewTab(tabs.Tab):
    name = _("Overview")
    slug = "overview"
    template_name = ("security_reports/_detail_overview.html")

    def get_context_data(self, request, **kwargs):
        return {"security_report": self.tab_group.kwargs['security_report']}


class VulnerabilitiesTab(tabs.TableTab):
    table_classes = (tables.VulnerabilitiesTable,)
    name = _("Vulnerabilities")
    slug = "vulnerabilities"
    template_name = "horizon/common/_detail_table.html"

    def get_vulnerabilities_data(self):
        vulnerabilities = self.tab_group.kwargs[
            'security_report'].vulnerabilities

        return json.loads(vulnerabilities).values()


class DetailsTabs(tabs.TabGroup):
    slug = "security_report_details"
    sticky = True
    tabs = (OverviewTab, VulnerabilitiesTab,)
