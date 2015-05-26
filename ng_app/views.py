from django.utils.translation import get_language
from django.views.generic import TemplateView
from ng_app.forms import ContactForm, FreeTrialForm


class PartialGroupView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        # update the context
        return context


class ContactView(TemplateView):
    """
    Contact page view.

    This view just renders the partial to angular

    If you're looking for the one which process the form search in
    api/views module.
    """
    template_name = 'ng_app/partials/sections/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context.update(
            contact_form=ContactForm(
                form_name='contact_form',
                scope_prefix='contact_data'))
        return context


class FreeTrialView(TemplateView):
    """
    Contact page view.

    This view just renders the partial to angular

    If you're looking for the one which process the form search in
    api/views module.
    """
    def get_context_data(self, **kwargs):
        context = super(FreeTrialView, self).get_context_data(**kwargs)
        context.update(
            free_trial_form=FreeTrialForm(
                form_name='contact_form',
                scope_prefix='contact_data'))
        return context