from django.db import models
from django.contrib.auth.models import User

class Curator(models.Model):
    class Meta:
        verbose_name = "Куратор (Подразделение)"
        verbose_name_plural = "Кураторы (Подразделения)"

    title = models.CharField(
        max_length=120,
        verbose_name="Куратор"
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'


class UserTypes(models.Model):
    class Meta:
        verbose_name = "Тип пользователя"
        verbose_name_plural = "Типы пользователя"

    title = models.CharField(
        max_length=120,
        verbose_name="Тип пользователя",
        help_text="Администратор, Куратор, БПиЭА, Пользователь, Экономист, Спкциалист АСЭЗ, Юрист"
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'


class CustomUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Пользователь")
    curator = models.ForeignKey(
        Curator,
        verbose_name="Подразделение (Куратор)",
        on_delete=models.DO_NOTHING
    )
    email = models.EmailField()
    name = models.CharField(
        max_length=150,
        verbose_name="Фамилия, Имя, Отчество"
    )
    position = models.CharField(
        max_length=200,
        verbose_name="Должность",
        null=True,
        blank=True
    )
    user_type = models.ForeignKey(
        UserTypes,
        verbose_name="Тип пользователя (Пользователь, Администратор, Куратор, Суперпользователь, БПиЭА, Юрист, Экономист, Специалист АСЭЗ)",
        on_delete=models.DO_NOTHING
    )
    blocked_status = models.BooleanField(
        default=True,
        verbose_name="Активный пользователь/Заблокированный"
    )

    def __str__(self):
        try:
            return str(self.user)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserActivityJournal(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.DO_NOTHING)
    date_time_of_activity = models.DateTimeField(
        verbose_name="Дата и время работы пользователя в системе"
    )
    activity = models.CharField(
        max_length=200,
        verbose_name="Действия пользователя в системе",
        blank=True,
        null=True
    )
    clicks = models.PositiveIntegerField(
        verbose_name="Количество кликов пользователя",
        blank=True,
        null=True
    )
    activity_system_module = models.CharField(
        max_length=100,
        verbose_name="Раздел системы",
        blank=True
    )

    def __str__(self):
        try:
            return 'Журнал действий пользователя: %s' % (self.user)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Журнал действий пользователя'
        verbose_name_plural = 'Журналы действий пользователя'


class FinanceCosts(models.Model):
    title = models.CharField(
        verbose_name="Название статьи",
        max_length=100
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Статья финансирования'
        verbose_name_plural = 'Статьи финансирования'


class PurchaseType(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Вид закупки (Конкурентная, неконкурентная)"
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Тип закупки'
        verbose_name_plural = 'Типы закупок'


class ActivityForm(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Вид деятельности"
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Вид деятельности'
        verbose_name_plural = 'Виды деятельности'


class StateASEZ(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Состояние АСЭЗ"
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Состояние АСЭЗ'
        verbose_name_plural = 'Состояние АСЭЗ'


class NumberPZTRU(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Номер пункта ПоЗТРУ"
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Номер пункта Положения о закупках товаров, работ, услуг ПАО "Газпром"'
        verbose_name_plural = 'Номера пунктов Положения о закупках товаров, работ, услуг ПАО "Газпром"'


class ContractStatus(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Статус договора"
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Статус договора'
        verbose_name_plural = 'Статусы договоров'


class Currency(models.Model):
    title = models.CharField(
        max_length=10,
        verbose_name="Валюта"
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Типы валют'


class ContractType(models.Model):
    title = models.CharField(
        max_length=150,
        help_text="Тип договора(Центр, Филиал)"
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Тип договора (Центр/Филиал)'
        verbose_name_plural = 'Типы договоров (Центр/Филиал)'


class ContractMode(models.Model):
    title = models.CharField(
        max_length=150,
        help_text="Вид договора (Основной, доп.соглашение)"
    )

    def __str__(self):
        try:
            return str(self.title)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Вид договора (Основной/ доп. соглашение)'
        verbose_name_plural = 'Виды договоров (Основной/ доп. соглашение)'


class Counterpart(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Контрагент"
    )
    email = models.EmailField()
    reg_addr = models.CharField(
        max_length=255,
        verbose_name="Юридический адрес"
    )
    UNP = models.CharField(
        max_length=100,
        verbose_name="УНП"
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Номер телефона"
    )

    def __str__(self):
        try:
            return '%s УНП: %s' % (self.name, str(self.UNP))
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Contract(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Наименование договора"
    )
    finance_cost = models.ForeignKey(
        FinanceCosts,
        on_delete=models.DO_NOTHING,
        verbose_name="Статья финансирования")
    curator = models.ForeignKey(
        Curator,
        on_delete=models.DO_NOTHING,
        verbose_name="Куратор"
    )
    contract_type = models.ForeignKey(
        ContractType,
        verbose_name="Тип договора",
        on_delete=models.DO_NOTHING,
        help_text="Филиал или центръ"
    )
    contract_mode = models.ForeignKey(
        ContractMode,
        verbose_name="Вид договора",
        on_delete=models.DO_NOTHING,
        help_text="Основной либо доп.согл.")
    purchase_type = models.ForeignKey(
        PurchaseType,
        verbose_name="Тип закупки",
        on_delete=models.DO_NOTHING,
        help_text="Вид закупки (конкурентная, неконкурентная)"
    )
    activity_form = models.ForeignKey(
        ActivityForm,
        verbose_name="Вид деятельности",
        on_delete=models.DO_NOTHING
    )
    stateASEZ = models.ForeignKey(
        StateASEZ,
        verbose_name="Состояние в Автоматизированной системе эллектронных закупок",
        on_delete=models.DO_NOTHING
    )
    number_ppz = models.CharField(
        max_length=150,
        verbose_name="Номер позиции плана закупок",
        null=True,
        blank=True
    )
    number_PZTRU = models.ForeignKey(
        NumberPZTRU,
        verbose_name="ПЗТРУ",
        help_text="Номер Положения о закупках товаров, работ, услуг",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    contract_status = models.ForeignKey(
        ContractStatus,
        verbose_name="Статус договора",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    plan_load_date_ASEZ = models.DateField(
        verbose_name="планируемая дата загрузки в АСЭЗ",
    )
    fact_load_date_ASEZ = models.DateField(
        verbose_name="фактическая дата загрузки в АСЭЗ",
        null=True,
        blank=True
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.DO_NOTHING,
        verbose_name="Валюта договора",
        blank=True,
        null=True
    )
    number_KGG = models.CharField(
        max_length=100,
        verbose_name="номер договора от центрального органа",
        null=True,
        blank=True
    )
    register_number_SAP = models.CharField(
        max_length=100,
        verbose_name="Регистрационный номер в САП",
        null=True,
        blank=True
    )
    contract_number = models.CharField(
        max_length=100,
        verbose_name="Номер договора",
        null=True,
        blank=True
    )
    plan_sign_date = models.DateField(
        verbose_name="Планируемая дата подписания договора"
    )
    fact_sign_date = models.DateField(
        verbose_name="Фактическая дата подписания договора",
        null=True,
        blank=True
    )
    start_date = models.DateField(
        verbose_name="дата начала контракта"
    )
    end_time = models.DateField(
        verbose_name="дата окончания",
        null=True, blank=True
    )
    counterpart = models.ForeignKey(
        Counterpart,
        on_delete=models.DO_NOTHING,
        verbose_name="Контрагент"
    )
    related_contract = models.ForeignKey(
        "Contract",
        on_delete=models.DO_NOTHING,
        verbose_name="Связанный договор",
        blank=True,
        null=True
    )
    contract_active = models.BooleanField(
        default=True,
        verbose_name="Действующий/Удаленный договор",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

    def __str__(self):
        try:
            return 'Договор %s, куратор %s, ст. фин %s' % (self.title,
                                                           self.curator,
                                                           self.finance_cost)
        except:
            return 'Ошибка в данных'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # TODO   contract_mode


class SumsRUR(models.Model):
    contract = models.ForeignKey(
        Contract,
        verbose_name="Контракт",
        on_delete=models.DO_NOTHING
    )
    start_max_price_ASEZ_NDS = models.DecimalField(
        verbose_name="стартовая цена АСЭЗ с НДС ",
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=20
    )
    currency_rate_on_load_date_ASEZ_NDS = models.DecimalField(
        verbose_name="Курс валюты на дату загрузки в бел.руб.",
        null=True,
        blank=True,
        decimal_places=10,
        max_digits=20
    )
    contract_sum_NDS_RUB = models.DecimalField(
        verbose_name="Сумма договора с НДС рос.руб.",
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=20
    )
    currency = models.ForeignKey(
        Currency,
        verbose_name="Валюта",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    delta_data_ASEZ = models.DecimalField(
        verbose_name="Отклонение от НМЦ в АСЭЗ",
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=20
    )
    #sum_byn = models.ForeignKey("SumsBYN", on_delete=models.DO_NOTHING)

    def __str__(self):
        try:
            return 'Показатели договора %s в российских рублях' % (self.contract)
        except:
            return 'Ошибка в данных'

    def save(self, *args, **kwargs):
        #self.sum_byn = self.sum_byn.contract_sum_with_NDS_BYN
        #sum_byn = SumsBYN.objects.filter(contract=self.contract).contract_sum_with_NDS_BYN
        #self.contract_sum_NDS_RUB = sum_byn * self.currency_rate_on_load_date_ASEZ_NDS
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Показатели договора в российских рублях'
        verbose_name_plural = 'Показатели договора в российских рублях'


class SumsBYN(models.Model):
    YEARS = [
        ("2018", "2018"),
        ("2019", "2019"),
        ("2020", "2020"),
        ("2021", "2021"),
        ("2022", "2022")
    ]
    PERIODS = [
        ("year", "year"),
        ("1quart", "1 quarter"),
        ("2quart", "2 quarter"),
        ("3quart", "3 quarter"),
        ("4quart", "4 quarter"),
        ("6months", "6months"),
        ("9months", "9months"),
        ("10months", "10months"),
        ("11months", "11months"),
        ("jan", "january"),
        ("feb", "february"),
        ("mar", "march"),
        ("apr", "april"),
        ("may", "may"),
        ("jun", "june"),
        ("jul", "july"),
        ("aug", "august"),
        ("sep", "september"),
        ("oct", "october"),
        ("nov", "november"),
        ("dec", "december")
    ]
    contract = models.ForeignKey(
        Contract,
        on_delete=models.DO_NOTHING,
        verbose_name="Контракт"
    )
    year = models.CharField(
        verbose_name="Год",
        choices=YEARS,
        max_length=4
    )
    period = models.CharField(
        choices=PERIODS,
        verbose_name="Период",
        max_length=15
    )
    plan_sum_SAP = models.DecimalField(
        verbose_name="Плановая сумма САП",
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=20
    )
    contract_sum_without_NDS_BYN = models.DecimalField(
        verbose_name="Сумма всего договора без НДС",
        default=0,
        decimal_places=2,
        max_digits=20
    )
    contract_sum_with_NDS_BYN = models.DecimalField(
        verbose_name="Сумма договора с НДС бел.руб.",
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=20
    )
    contract_total_sum_with_sub_BYN = models.DecimalField(
        verbose_name='Общая сумма договора всего с доп соглашениями, б.р. без ндс',
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=20
    )
    forecast_total = models.DecimalField(
        verbose_name='Прогноз, всего',
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=20
    )
    economy_total = models.DecimalField(
        verbose_name='Экономия по заключенному договору, всего',
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=20
    )
    fact_total = models.DecimalField(
        verbose_name='Факт, всего',
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=20
    )
    economy_contract_result = models.DecimalField(
        verbose_name='Экономия по результатам исполнения договоров всего',
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=20
    )
    total_sum_unsigned_contracts = models.DecimalField(
        verbose_name='Сумма средств по незаключенным договорам',
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=20
    )
    economy_total_absolute = models.DecimalField(
        verbose_name='Абсолютная экономия по договору, всего',
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=20
    )

    def __str__(self):
        try:
            return 'Показатели договора %s в белорусских рублях' % (self.contract)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Показатели договора в белорусских рублях'
        verbose_name_plural = 'Показатели договора в белорусских рублях'


class ContractPaymentSchedule(models.Model):
    contract = models.ForeignKey(
        Contract,
        verbose_name="Договора",
        on_delete=models.CASCADE
    )
    payment_date = models.DateField(
        verbose_name="Дата платежа"
    )

    class Meta:
        verbose_name = 'График платежей по договору'
        verbose_name_plural = 'Графики платежей по договору'

    def __str__(self):
        try:
            return 'График платежей по договору : %s, оплата до: %s' % (self.contract,
                                                                        self.payment_date)
        except:
            return 'Ошибка в данных'


class ContractRemarks(models.Model):
    contract = models.ForeignKey(
        Contract,
        verbose_name="Контракт",
        on_delete=models.CASCADE
    )
    remark_text = models.TextField(
        verbose_name="Текст примечания"
    )

    class Meta:
        verbose_name = 'Примечание к договору'
        verbose_name_plural = 'Примечания к договору'

    def __str__(self):
        try:
            return 'Примечание к Договору %s' % (self.contract)
        except:
            return 'Ошибка в данных'


class Planning(models.Model):
    # PERIODS = [
    #     ("year", "year"),
    #     ("1quart", "1 quarter"),
    #     ("2quart", "2 quarter"),
    #     ("3quart", "3 quarter"),
    #     ("4quart", "4 quarter")
    # ]

    YEARS = [
        ("2018", "2018"),
        ("2019", "2019"),
        ("2020", "2020"),
        ("2021", "2021"),
        ("2022", "2022")
    ]
    FinanceCosts = models.ForeignKey(
        FinanceCosts,
        verbose_name="Статья финансирования",
        on_delete=models.DO_NOTHING
    )
    curator = models.ForeignKey(
        Curator,
        verbose_name="Куратор",
        on_delete=models.DO_NOTHING
    )
    year = models.CharField(
        verbose_name="Год",
        choices=YEARS,
        max_length=15
    )
    # period = models.PositiveIntegerField(
    #     choices=PERIODS,
    #     verbose_name="Период"
    # )
    # total = models.DecimalField(
    #     verbose_name="Сумма, Лимит средств",
    #     default=0,
    #     decimal_places=2,
    #     max_digits=20
    # )
    currency = models.ForeignKey(
        Currency,
        verbose_name="Валюта",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )
    q_1 = models.DecimalField(
        verbose_name="Сумма лимита 1 квартал",
        max_digits=20,
        decimal_places=2,
        default=0,
        null=True
    )
    q_2 = models.DecimalField(
        verbose_name="Сумма лимита 2 квартал",
        max_digits=20,
        decimal_places=2,
        default=0,
        null=True
    )
    q_3 = models.DecimalField(
        verbose_name="Сумма лимита 3 квартал",
        max_digits=20,
        decimal_places=2,
        default=0,
        null=True
    )
    q_4 = models.DecimalField(
        verbose_name="Сумма лимита 4 квартал",
        max_digits=20,
        decimal_places=2,
        default=0,
        null=True
    )
    q_all = models.DecimalField(
        verbose_name="Сумма лимита за весь год",
        max_digits=20,
        decimal_places=2,
        default=0,
        null=True
    )
    def __str__(self):
        try:
            return 'Планирование %s год, по куратору %s, ст. фин %s' % (self.year, self.curator, self.FinanceCosts)
        except:
            return 'Ошибка в данных'

    def get_finance_costs(self, *args, **kwargs):
        # all_finance_costs = Planning.objects.filter(FinanceCosts=self.FinanceCosts)
        # if not all_finance_costs:
        all_finance_costs = Planning.create(FinanceCosts=self.FinanceCosts, year=self.year, curator='All')
        return all_finance_costs



    def save(self, *args, **kwargs):
        self.q_all = self.q_1 + self.q_2 + self.q_3 + self.q_4
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Планирование'
        verbose_name_plural = 'Планирование'


class AnalysisPlanFulfilmentSums(models.Model):
    PERIODS = [
        ("year", "year"),
        ("1quart", "1 quarter"),
        ("2quart","2 quarter"),
        ("3quart", "3 quarter"),
        ("4quart", "4 quarter"),
        ("6months", "6months"),
        ("9months", "9months")
    ]
    year = models.DateField(
        verbose_name="Год"
    )
    period = models.PositiveIntegerField(
        choices=PERIODS,
        verbose_name="Анализируемый период"
    )
    finance_cost = models.ForeignKey(
        FinanceCosts,
        on_delete=models.DO_NOTHING,
        verbose_name="Статья финансирования"
    )
    curator = models.ForeignKey(
        Curator,
        on_delete=models.DO_NOTHING,
        verbose_name="Куратор/Подразделение"
    )
    plannned_sum = models.DecimalField(
        verbose_name="Лимит средств (запланировано БПиЭА)",
        decimal_places=2,
        max_digits=20
    )
    contract_planned_sum = models.DecimalField(
        verbose_name="План по всем договорам",
        decimal_places=2,
        max_digits=20
    )
    signed_contract_sum = models.DecimalField(
        verbose_name="Сумма заключенных договоров",
        decimal_places=2,
        max_digits=20
    )
    fact_contract_sum = models.DecimalField(
        verbose_name="Фактическое выполнение всех договоров",
        decimal_places=2,
        max_digits=20
    )
    forecast_contract_sum = models.DecimalField(
        verbose_name="Прогноз выполнения всех договоров",
        decimal_places=2,
        max_digits=20
    )
    percent_of_contracts_fulfilment = models.DecimalField(
        verbose_name="Процент выполнения плана",
        decimal_places=2,
        max_digits=20
    )

    def __str__(self):
        try:
            return 'Аналитика выполнения плана, суммы,  за %s год, %s квартал по куратору %s, ст. фин %s' % (self.year,
                                                                                                             self.period,
                                                                                                             self.curator,
                                                                                                             self.finance_cost)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Анализ выполнения плана, суммы'
        verbose_name_plural = 'Анализ выполнения плана, суммы'


class AnalysisPlanFulfilmentContractsQuantity(models.Model):
    PERIODS = [
        ("year", "year"),
        ("1quart", "1 quarter"),
        ("2quart","2 quarter"),
        ("3quart", "3 quarter"),
        ("4quart", "4 quarter"),
        ("6months", "6months"),
        ("9months", "9months")
    ]

    year = models.DateField(
        verbose_name="Год"
    )
    period = models.PositiveIntegerField(
        choices=PERIODS,
        verbose_name="Анализируемый период"
    )
    finance_cost = models.ForeignKey(
        FinanceCosts,
        on_delete=models.DO_NOTHING,
        verbose_name="Статья финансирования"
    )
    curator = models.ForeignKey(
        Curator,
        on_delete=models.DO_NOTHING,
        verbose_name="Куратор/Подразделение"
    )
    contract_type = models.ForeignKey(
        ContractType,
        on_delete=models.DO_NOTHING,
        verbose_name="Центр/Филиал"
    )
    contracts_quantity_total = models.PositiveIntegerField(
        verbose_name="Общее количество договоров"
    )
    signed_contracts_quantity = models.PositiveIntegerField(
        verbose_name="Количество заключенных договоров"
    )

    def __str__(self):
        try:
            return 'Аналитика выполнения плана, количество договоров, за %s год, %s квартал по куратору %s, ст. фин %s' % (self.year,
                                                                                                                           self.period,
                                                                                                                           self.curator,
                                                                                                                           self.finance_cost)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Анализ выполнения плана, количество договоров'
        verbose_name_plural = 'Анализ выполнения плана, количество договоров'


class DeltaAnalysis(models.Model):
    PERIODS = [
        ("year", "year"),
        ("1quart", "1 quarter"),
        ("2quart", "2 quarter"),
        ("3quart", "3 quarter"),
        ("4quart", "4 quarter"),
        ("6months", "6months"),
        ("9months", "9months")
    ]

    year = models.DateField(
        verbose_name="Год"
    )
    period = models.PositiveIntegerField(
        choices=PERIODS,
        verbose_name="Анализируемый период"
    )
    finance_cost = models.ForeignKey(
        FinanceCosts,
        on_delete=models.DO_NOTHING,
        verbose_name="Статья финансирования"
    )
    curator = models.ForeignKey(
        Curator,
        on_delete=models.DO_NOTHING,
        verbose_name="Куратор/Подразделение"
    )
    delta_limit_plan_sum_sap = models.DecimalField(
        verbose_name="Отклонение: Лимит - Плановая сумма САП",
        decimal_places=2,
        max_digits=20
    )
    delta_limit_signed_contracts_sum = models.DecimalField(
        verbose_name="Отклонение: Лимит - Сумма заключенных договоров",
        decimal_places=2,
        max_digits=20
    )
    delta_limit_forecast = models.DecimalField(
        verbose_name="Отклонение: Лимит - Прогноз выполнения договоров",
        decimal_places=2,
        max_digits=20
    )
    delta_limit_fact = models.DecimalField(
        verbose_name="Отклонение: Лимит - Фактическое выполнение договоров",
        decimal_places=2,
        max_digits=20
    )
    delta_plan_sum_sap_signed_contracts_sum = models.DecimalField(
        verbose_name="Отклонение: Плановая сумма САП - Сумма заключенных договоров",
        decimal_places=2,
        max_digits=20
    )
    delta_plan_sum_sap_forecast = models.DecimalField(
        verbose_name="Отклонение: Плановая сумма САП - Прогноз по всем договорам",
        decimal_places=2,
        max_digits=20
    )
    delta_plan_sum_sap_forecast_signed_contracts = models.DecimalField(
        verbose_name="Отклонение: Плановая сумма САП - Прогноз по заключенным договорам",
        decimal_places=2,
        max_digits=20
    )
    delta_plan_sum_sap_fact = models.DecimalField(
        verbose_name="Отклонение: Плановая сумма САП - Фактическое выполнение договоров",
        decimal_places=2,
        max_digits=20
    )
    delta_signed_contracts_sum_forecat = models.DecimalField(
        verbose_name="Отклонение: Сумма заключенных договоров - Прогноз исполнения заключенных договоров",
        decimal_places=2,
        max_digits=20
    )
    delta_signed_contracts_sum_fact = models.DecimalField(
        verbose_name="Отклонение: Сумма заключенных договоров - Фактическое исполнение",
        decimal_places=2,
        max_digits=20
    )
    delta_forecast_fact = models.DecimalField(
        verbose_name="Отклонение: Прогноз по всем договорам - Фактическое исполнение",
        decimal_places=2,
        max_digits=20
    )
    def __str__(self):
        try:
            return 'Аналитика отклонений по всем договорам за %s год, %s квартал по куратору %s, ст. фин %s' % (self.year,
                                                                                                                self.period,
                                                                                                                self.curator,
                                                                                                                self.finance_cost)
        except:
            return 'Ошибка в данных'

    class Meta:
        verbose_name = 'Анализ отклонений по всем договорам'
        verbose_name_plural = 'Анализ отклонений по всем договорам'








