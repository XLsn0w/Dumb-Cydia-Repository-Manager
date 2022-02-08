# coding=utf-8

"""
DCRM - Darwin Cydia Repository Manager
Copyright (C) 2017  WU Zheng <i.82@me.com> & 0xJacky <jacky-943572677@qq.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Notice: You have used class-based views, that's awesome.
        If not necessary, you can try function-based views.
        You may add lines above as license.
"""

from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.template.context_processors import csrf

from WEIPDCRM.models.package import Package


def search_view(request):
    context = {}
    if request.POST:
        context.update(csrf(request))
        context['request'] = request.POST['package']
        context['package_list'] = Package.objects.filter(c_name__icontains=request.POST['package'])[:24]
    else:
        return HttpResponseBadRequest()
    return render(request, 'search.html', context)
