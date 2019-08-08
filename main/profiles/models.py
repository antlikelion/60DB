from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser

class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(blank=True, null=True)
    # 3.인우 : 장고에서 ImageField를 쓰기 위해서는 pillow 패키지가 필수라고 합니다.
    # requirements.txt에 freeze시켜뒀습니다.
    # requriements.txt에 있는 모든 항목을 다운받으려면
    # pip install -r requirements.txt
    # 를 실행하면 됩니다.

    male = "남성"
    female = "여성"
    gender_choices = (
        (male, '남성'), (female, "여성")
    )
    gender = models.CharField(
        max_length=6, choices=gender_choices, blank=True, null=True)

    birth_date = models.CharField(max_length=30, blank=True, null=True)

    height = models.CharField(max_length=30, default=160, blank=True, null=True)
    # 5.인우 : validator는 나중에 좀 더 손봐야 할 것 같습니다. 장난으로 키 막 300 이렇게 적을까봐 일단
    # 넣어봤어요.

    weight = models.CharField(max_length=30, default=60, blank=True, null=True)
    # 6.인우 : validator는 나중에 좀 더 손봐야 할 것 같습니다. 장난으로 몸무게 막 300 이렇게 적을까봐 일단
    # 넣어봤어요.

    name = models.CharField(max_length=10, default="")

    # 과거력

    # 이전에 건강검진을 받은 적이 있나요?
    had_checkup = models.CharField(max_length=30, default="", blank=True, null=True)

    # 몇 년 전에 받았나요?
    under_one = "1년 이내"
    one_to_three = "1-3년"
    three_to_five = "3-5년"
    five_to_ten = "5-10년"
    over_ten = "10년 이상"
    how_long_before = (
        (under_one, '1년 이내'), (one_to_three, "1-3년"), (three_to_five,
                                                       "3-5년"), (five_to_ten, "5-10년"), (over_ten, "10년 이상")
    )
    had_checkup_true = models.CharField(
        max_length=6, choices=how_long_before, blank=True, null=True)

    # 이전에 진단받은 병이 있나요?
    high_blood_pressure = "고혈압"
    hepatitis = "간염"
    tuberculosis = "결핵"
    none = "없음"
    etc = "기타"
    disease_list = (
        (high_blood_pressure, '고혈압'), (hepatitis,
                                       '간염'), (tuberculosis, '결핵'), (none, '없음'), (etc, '기타')
    )
    diagnosed_disease = models.CharField(max_length=3, choices=disease_list, blank=True, null=True)

    # 드시고 계시는 약이 있나요?
    taking_medicine = models.CharField(max_length=30, default=False, blank=True, null=True)

    # 드시고 계신 약물을 알려주세요
    what_medicine = models.CharField(max_length=20, blank=True, null=True)
    # 복용하고 있는 약물이 복수라면...? 필드를 조정하거나 max_length를 조정해야 하나..?

    # 가족분들이 진단 받은 병이 있나요?
    family_history = models.CharField(max_length=3, choices=disease_list, blank=True, null=True)

    # 사회력

    # 술을 드시나요?
    drinking = models.CharField(max_length=30, default="", blank=True, null=True)

    # 매주 몇 병 드시나요?
    drinking_per_week = models.CharField(
        max_length=30, blank=True, null=True)

    # 흡연하시나요?
    smoking_true = "예"
    smoking_false = "아니오"
    smoking_quit = "끊었음"
    do_you_smoke = (
        (smoking_true, "예"), (smoking_false, "아니오"), (smoking_quit, "끊었음")
    )
    smoking = models.CharField(max_length=3, choices=do_you_smoke, blank=True, null=True)

    # 몇년째 피고 계신가요?
    how_long_smoking = models.CharField(max_length=30, default=0, blank=True, null=True)

    # 몇 갑씩 피시나요
    how_much_smoking = models.CharField(max_length=30, default=0, blank=True, null=True)

    # 직업이 무엇인가요?
    job = models.CharField(max_length=20, blank=True, null=True)
    # 직업을 꼭 말하고 싶지 않을 수도 있죠

    # 다음 중 해당사항에 체크해주세요
    stress = "스트레스를 많이 받는 편"
    irregular_meals = "식사 불규칙"
    greasy_meals = "기름진 음식을 많이 먹음"
    irregular_sleep = "수면시간 불규칙"
    bad_habits = (
        (stress, "스트레스를 많이 받는 편"), (irregular_meals, "식사 불규칙"), (greasy_meals,
                                                                 "기름진 음식을 많이 먹음"), (irregular_sleep, "수면시간 불규칙")
    )
    relevant_data = models.CharField(
        max_length=13, choices=bad_habits, blank=True, null=True)



    def __str__(self):
        return self.name
        # return str(self.user)
