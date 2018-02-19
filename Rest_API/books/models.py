from django.db import models
# Create your models here.


class Publisher(models.Model):
	name    = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city    = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	# object 객체 출력시 사용할 이름
	def __str__(self):
		return self.name


class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(blank = True,   # blank도 유효한 값 인정, cf) blank = False (default)
							  verbose_name = 'e-mail')  # cf) admin 출력명만 변경, 컬럼명 변경은 X

	# object 객체 출력시 사용할 이름
	def __str__(self):
		return u'%s %s'%(self.first_name, self.last_name)


class BookManager(models.Manager):
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()

class DjangoBookManager(models.Manager):
	def get_queryset(self):
		return super(DjangoBookManager, self).get_queryset().filter(title='Django CookBook')

class Book(models.Model):
	title = models.CharField(max_length=100)

	# 다 vs 다 Join (admin : + Join을 설정)
	author = models.ManyToManyField(Author)
	publication_date = models.DateField(blank=True, null=True)

	# 기본키 연결 (admin : drop down 메뉴)
	# django2.0 추가 (외래키 의존) : 기본키가 삭제시, 의존된 DB도 함께 삭제된다
	publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE)
	# django2.0 추가 (외래키 독립) : 기본키와 별도로 DB가 남는다
	# publisher = models.ForeignKey('Publisher',on_delete=models.PROTECT)

	django_objects = DjangoBookManager()
	num_pages = models.IntegerField(blank=True, null=True)
	objects = BookManager()   # 위에서 class 선언된 뒤 실행

	# object 객체 출력시 사용할 이름
	def __str__(self):
		return self.title