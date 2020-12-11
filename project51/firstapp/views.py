from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render(request=request, template_name='firstapp/homepage.html')


def display_physics_information(request):
	main_msg = 'updated physics Information'

	msg1 = 'Explore the motion of plants, animals, lightning, satellites, charges, light and empty space itself! Be fascinated by molecular motors, black holes, the beauty of nature and the simplicity of how it works: Explore the principle of cosmic laziness – least action –, the maximum speed, the largest distance, the highest power, and gauge symmetry, the symmetry that explains electric motors, radioactivity and quarks!'

	msg2 = 'The volumes of the 2021 edition tell about the race to make images floating in mid-air with lasers, tell about the sound of falling batteries, tell about how to measure images on the eyes retina in living humans, tell about the sounds deep inside the Earth, show the possibilities of very long baseline interferometry for testing general relativity, includes the new definition of the kilogram and the other SI units, lists the effects of weightlessness on cosmonauts, show how to multiply with fingers, explain how physics helps with basketball, and present many other stunning images, facts and stories about motion of things, shadows, light, stars, planets, black holes and quantum particles.'

	msg3 = 'https://techniumscience.com/index.php/technium/article/view/1036?gclid=CjwKCAjw8-78BRA0EiwAFUw8LEgR7qWHfaY2Wv8gV_lnewpuFLo1c7-UYn0jbzHI6HLkE4Df1c8UoBoCWX8QAvD_BwE'

	my_dict = {'main_msg':main_msg,'msg1':msg1,'msg2':msg2 ,'msg3':msg3}
	return render(request=request, template_name='firstapp/physics.html',context=my_dict)


def display_chemistry_information(request):
	main_msg = 'updated chemistry Information'

	msg1 = 'Titanium is extremely sensitive to small amounts of oxygen, which can lead to markedly decreased ductility of the material. Materials scientists therefore aim to lower the costs of purifying titanium, while avoiding the poisoning ...'
	msg2 = 'Polypropylene (PP) is one of the most widely used plastics in the world. By controlling the spatial orientation of the propylene building blocks and additional polar components, it should be possible to create a new generation ..'

	my_dict = {'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request=request, template_name='firstapp/chemistry.html',context=my_dict)


def display_social_information(request):
	main_msg = 'updated social  Information'

	msg1 = 'Modi will become PM for next election also!!!'
	msg2 = 'TikTok Stars Win Injunction Against White House Executive Order, Keeping the App Running the US'

	my_dict = {'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request=request, template_name='firstapp/social.html',context=my_dict)
