from django.db import models
from django.utils import timezone
import random
# Create your models here.

class GuessNumbers(models.Model):
    # id(PK)는 자동생성
    name = models.CharField(max_length=24)
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255, default='[1,2,3,4,5,6]') # 로또 번호 리스트
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()
    
    def generate(self):
        self.lottos = ""
        origin = list(range(1,46))
        
        for _ in range(0,self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + "\n"
            
        self.update_date = timezone.now()
        self.save()
     
    #GuessNumbers를 print했을 때, 출력되는 값   
    def __str__(self):
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)
