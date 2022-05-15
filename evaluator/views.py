from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView, DetailView

from evaluator.models import Classroom


class ClassList(LoginRequiredMixin, ListView):
    template_name = 'evaluator/class_list.html'
    queryset = Classroom.objects.all()


class StudentList(LoginRequiredMixin, ListView):
    template_name = 'evaluator/student_list.html'
    queryset = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = [
            {
                'name': 'Juho Hong',
                'id': '21300833',
                'scores': [20, 1, 0, 90]
            },
            {
                'name': 'Chanhyo Lee',
                'id': '21700589',
                'scores': [19, 0, 1, 95]
            },
            {
                'name': 'BoYoung Yun',
                'id': '21800486',
                'scores': [17, 0, 3, 91]
            },
            {
                'name': 'Hyogyung Seo',
                'id': '21900371',
                'scores': [20, 0, 0, 98]
            },
            {
                'name': 'Seulgi Jeong',
                'id': '21900667',
                'scores': [20, 0, 0, 95]
            }
        ]

        context['students'] = students
        return context


class AssignmentUpload(LoginRequiredMixin, ListView):
    template_name = 'evaluator/assignment_upload.html'
    queryset = []

# class AssignmentUpload(LoginRequiredMixin, FormView):
#     template_name = 'evaluator/assignment_upload.html'
#     form_class = None


class EvaluationResult(LoginRequiredMixin, ListView):
    template_name = 'evaluator/evaluation_result.html'
    queryset = []

# class EvaluationResult(LoginRequiredMixin, DetailView):
#     template_name = 'evaluator/evaluation_result.html'
#     object = None

class Logout(LoginRequiredMixin, ListView):
    template_name = 'account/logout.html'
    queryset = []


class ClassDetail(LoginRequiredMixin, ListView):
    template_name = 'evaluator/class_detail.html'
    queryset = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = [
            {
                'title': 'Assignment1',
                'duedate': '2022/05/29',
                'activate': 'active',
                'result': 'show result',
            },
        ]

        context['students'] = students
        return context

