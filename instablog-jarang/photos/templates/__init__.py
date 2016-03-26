from django import template

register = template.Library()

@register.filter(name='did_like')
#함수이름인 did_like로 지정하지 않아도된다
#name='did_like'를 생략하면 함수의 이름을 그대로 사용하게 됨
def did_like(photo, user):
	return photo.like_set.filter(user=user, status=True).exists()