from django.shortcuts import render, HttpResponse

# Create your views here.

def show_form(request):
    '''Show the contact form'''

    template_name = "formdata/form.html"

    return render(request, template_name)


def submit(request):
    '''
    Handle the form submission
    Read the form data from the request,
    and send it back to a template
    '''

    template_name = 'formdata/confirmation.html'
    print(request)


    if request.POST: # this is only true if the request is POST
        print(request.POST)
        # read the form data into python variables, calling from 
        # dictionaries by name set by us in base.html

        name = request.POST['name']
        fav_color = request.POST['fav_color']

        # package the form data up as context variables for the template
        context = {
            'name': name,
            'fav_color': fav_color,
        }

        return render(request, template_name, context)


    ## handle GET request on this URL
    # an 'ok' solution...
    # return HttpResponse('Nope.')

    ## a 'better' solution (still will show the wrong url)
    # template_name = "formdata/form.html"
    # return render(request, template_name)

    ## a better solution (use redirect)
    return redirect("show_form")
