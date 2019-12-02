from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import Residence, Review
from numpy import random


def page_info_generater(pages: Paginator, page_num) -> dict:
    page_num = int(page_num)
    num_pages = pages.num_pages
    single_page = pages.get_page(page_num)
    page_info = {
        'cur_page_num': page_num,
        'cur_page_info': single_page,
        'num_pages': num_pages,
    }
    if page_num <= 3:
        if num_pages - page_num <= 2:
            page_info['page_lr'] = [i for i in range(1, num_pages+1)]
        else:
            page_info['page_lr'] = [i for i in range(1, page_num+3)]
    elif num_pages - page_num <= 2:
        page_info['page_lr'] = [i for i in range(page_num-2, num_pages+1)]
    else:
        page_info['page_lr'] = [i for i in range(page_num-2, page_num+3)]

    if 1 in page_info['page_lr']:
        page_info['hide_left_dots'] = True
        page_info['page_lr'].remove(1)
    elif 2 in page_info['page_lr']:
        page_info['hide_left_dots'] = True
    else:
        page_info['hide_left_dots'] = False

    if num_pages in page_info['page_lr']:
        page_info['hide_right_dots'] = True
        page_info['page_lr'].remove(num_pages)
    elif num_pages - 1 in page_info['page_lr']:
        page_info['hide_right_dots'] = True
    else:
        page_info['hide_right_dots'] = False

    if num_pages == 1:
        page_info['hide_right_dots'] = True
    return page_info


def property_candidate_generator(candidate, search_form):
    apt_location = search_form['apt-location']
    apt_type = search_form['option-apt-type']
    apt_bedroom = search_form['option-apt-bedroom']
    apt_bathroom = search_form['option-apt-bathroom']
    apt_price = search_form['option-apt-price']

    if apt_location:
        filter_apt_location = Q(cmtid_id__cmtname__icontains=apt_location) | \
                              Q(cmtid_id__sttid_id__sttname__icontains=apt_location) | \
                              Q(cmtid_id__sttid_id__ctyid_id__ctyname__icontains=apt_location)
    else:
        filter_apt_location = Q()

    if apt_type == 'all':
        filter_apt_type = Q()
    else:
        filter_apt_type = Q(rsdtype=apt_type)

    if apt_bedroom == 'all':
        filter_apt_bedroom = Q()
    else:
        filter_apt_bedroom = Q(rsdbedroom=apt_bedroom)

    if apt_bathroom == 'all':
        filter_apt_bathroom = Q()
    else:
        filter_apt_bathroom = Q(rsdbathroom=apt_bathroom)

    if apt_price == 'all':
        filter_apt_price = Q()
    else:
        lower, upper = apt_price.split('-')
        filter_apt_price = Q(rsdprice__gte=lower) & Q(rsdprice__lte=upper)

    filtered = candidate.filter(filter_apt_location, filter_apt_price,
                                filter_apt_type, filter_apt_bedroom,
                                filter_apt_bathroom,
                                )
    return filtered


# Create your views here.
def index(request):
    ppt = Residence.objects.exclude(rsdbedroom=0).exclude(rsdbedroom__isnull=True)
    buffer = random.choice(ppt, 9, replace=False)
    ppt_show = {"properties_rand_%d" % (i+1): pr for i, pr in enumerate(buffer)}
    return render(request, "index.html", ppt_show)


def agent(request):
    return render(request, "agent.html")


def properties(request):
    ppt = Residence.objects.exclude(rsdbedroom=0).exclude(rsdbedroom__isnull=True).order_by('rsdid')

    if 'apt-location' in request.GET.keys():
        search_form = request.GET
        filtered = property_candidate_generator(ppt, search_form)
        pages = Paginator(filtered, 9)
        if 'page' in search_form:
            payload = page_info_generater(pages, search_form['page'])
        else:
            payload = page_info_generater(pages, 1)
        return render(request, "properties.html", payload)
    elif 'page' in request.GET.keys():
        pages = Paginator(ppt, 9)
        payload = page_info_generater(pages, request.GET['page'])
        return render(request, "properties.html", payload)
    else:
        pages = Paginator(ppt, 9)
        payload = page_info_generater(pages, 1)
        return render(request, "properties.html", payload)


def properties_single(request):
    if 'rsdid' in request.GET:
        ppt = Residence.objects.filter(rsdid=request.GET['rsdid'])[0]
        cmtid = ppt.cmtid.cmtid
        rvw_info = Review.objects.filter(cmtid__cmtid=cmtid)
        rate_group = rvw_info.values('rvwrate').annotate(count_rvw_rate=Count('rvwrate'))

        k1, k2 = 'rvwrate', 'count_rvw_rate'
        rate_result = {d[k1]: d[k2] for d in rate_group}
        for i in [1, 2, 3, 4, 5]:
            if i not in rate_result:
                rate_result[i] = 0

        payload = {
            'property_info': ppt,
            'rvw_info': rvw_info,
            'rate_result': rate_result,
        }
        return render(request, "properties-single.html", payload)
    else:
        return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")