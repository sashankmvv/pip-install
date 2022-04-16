from user.models import Profile
def base_user(request):
    profile=Profile.objects.filter().first()
    
    return {
        'profile':profile
    }
