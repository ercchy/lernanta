from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
  url(r'^$', 'projects.views.project_list',
      name='projects_gallery'),
  url(r'^create/$', 'projects.views.create',
      name='projects_create'),
  url(r'^(?P<slug>[\w-]+)/$', 'projects.views.show',
      name='projects_show'),
  url(r'^(?P<slug>[\w-]+)/contact_organizers/$',
      'projects.views.contact_organizers',
      name='projects_contact_organizers'),

  # Project Content URLs
  (r'^(?P<slug>[\w-]+)/content/', include('content.urls')),

  # Project Edit URLs
  url(r'^(?P<slug>[\w-]+)/edit/$', 'projects.views.edit',
      name='projects_edit'),
  url(r'^(?P<slug>[\w-]+)/edit/image/$',
      'projects.views.edit_image',
      name='projects_edit_image'),
  url(r'^(?P<slug>[\w-]+)/edit/ajax_image/$',
      'projects.views.edit_image_async',
      name='projects_edit_image_async'),
  url(r'^(?P<slug>[\w-]+)/edit/links/$',
      'projects.views.edit_links',
      name='projects_edit_links'),       
  url(r'^(?P<slug>[\w-]+)/edit/links/(?P<link>\d+)/edit/$',
      'projects.views.edit_links_edit',
      name='projects_edit_links_edit'),                               
  url(r'^(?P<slug>[\w-]+)/edit/links/(?P<link>\d+)/delete/$',
      'projects.views.edit_links_delete',
      name='projects_edit_links_delete'),
  url(r'^(?P<slug>[\w-]+)/edit/participants/$',
      'projects.views.edit_participants',
      name='projects_edit_participants'),
  url(r'^(?P<slug>[\w-]+)/edit/participants/(?P<username>[\w\-\. ]+)/delete/$',
      'projects.views.edit_participants_delete',
      name='projects_edit_participants_delete'),
  url(r'^(?P<slug>[\w-]+)/edit/participants/(?P<username>[\w\-\. ]+)/make_organizer/$',
      'projects.views.edit_participants_make_organizer',
      name='projects_edit_participants_make_organizer'),
  url(r'^(?P<slug>[\w-]+)/edit/participants/matching_non_participants/$',
      'projects.views.matching_non_participants',
      name='matching_non_participants'),
  url(r'^(?P<slug>[\w-]+)/edit/status/$',
      'projects.views.edit_status',
      name='projects_edit_status'),
)
