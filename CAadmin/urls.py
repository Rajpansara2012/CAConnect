from django.urls import path
from . import views
app_name = "CAadmin"


urlpatterns = [
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("contact-us", views.contact_us, name="contact_us"),
    path("client-add", views.client_add, name="client_add"),
    path("client-list", views.client_list, name="client_list"),
    path("show-client", views.show_client, name="show_client"),
    path("change-status", views.change_status, name="change_status"),
    path("client-detail/<int:client_id>",
         views.client_detail, name="client_detail"),
    path("client-edit/<int:client_id>",
         views.client_edit, name="client_edit"),
    path("delete_client/<int:client_id>",
         views.delete_client, name="delete_client"),
    path("CAsignup", views.ca_signup, name="ca_signup"),
    path("employees-list", views.employees_list, name="employees_list"),
    path("employee-create", views.employee_create, name="employee_create"),
    path("employees-details/<int:employee_id>",
         views.employees_details, name="employees_details"),
    path("employee-edit/<int:employee_id>",
         views.employee_edit, name="employee_edit"),
    path("delete-employee/<int:employee_id>",
         views.delete_employee, name="delete_employee"),
    path("client-detail/add_personal/<int:client_id>",
         views.add_personal, name="add_personal"),
    path("client-detail/add_general/<int:client_id>",
         views.add_general, name="add_general"),
    path("client-detail/download_per_file/<int:file_id>",
         views.download_per_file, name="download_per_file"),
    path("client-detail/download_gen_file/<int:file_id>",
         views.download_gen_file, name="download_gen_file"),
    path("client-detail/view_per_file/<int:file_id>",
         views.view_per_file, name="view_per_file"),
    path("client-detail/view_gen_file/<int:file_id>",
         views.view_gen_file, name="view_gen_file"),
    path("client-detail/delete_per_file/<int:file_id>/<int:client_id>",
         views.delete_per_file, name="delete_per_file"),
    path("client-detail/delete_gen_file/<int:file_id>/<int:client_id>",
         views.delete_gen_file, name="delete_gen_file"),
    path("task-list", views.task_list, name="task_list"),
    path("get-task-details/", views.get_task_details, name="get_task_details"),
    path("update-task-status/", views.update_task_status,
         name="update_task_status"),
    path("update-task/<int:task_id>",
         views.update_task, name="update_task"),
    path("change_password/<int:client_id>",
         views.change_password, name="change_password"),
    path("change_employee_password/<int:employee_id>",
         views.change_employee_password, name="change_employee_password"),

    path("inquiry-list", views.inquiry_list, name="inquiry_list"),
    path("inquiry-view/<int:inquiry_id>",
         views.inquiry_view, name="inquiry_view"),
    path("inquiry-view/inquiry-delete/<int:inquiry_id>",
         views.inquiry_delete, name="inquiry_delete"),
    path("inquiry-delete/<int:inquiry_id>",
         views.inquiry_delete, name="inquiry_delete"),

    path("announcement-page", views.announcement_page, name="announcement_page"),
    path("get-announcement", views.get_announcement, name="get_announcement"),
    path("update-announcement/<int:announcement_id>",
         views.update_announcement, name="update_announcement"),

    path("delete_announcement/<int:announcement_id>",
         views.delete_announcement, name="delete_announcement"),
    path("logout", views.logout, name="logout"),
]
