# from django.conf import settings
from .models import Upload 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Upload
from django.core.files import uploadedfile


class UploadView(CreateView):
    model = Upload
    fields = ['upload_file', ]
    success_url = reverse_lazy('fileupload')

    # UNCOMMENT THE FOLLOWING 6 LINES AND CHANGE PATH ACCORDING TO NEED 
    # fo = open(r'media\testfile2.txt', 'r')
    # for x in fo.read():
    #     y = x.upper()
    #     # print(y)
    #     fo1 = open(r'media\testfile2.txt', 'a')
    #     fo1.write(y)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()
    
        # for x in uploadedfile.UploadedFile.read:
        #     y = x.upper()
        #     fo1 = open(settings.BASE_DIR, 'test', 'w')
        #     fo1.write(y)
        #     fo1.close()
        return context
      

        