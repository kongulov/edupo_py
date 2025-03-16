from django.utils.translation import gettext_lazy as _

USERTYPE = (
    (1, _('Admin')),
    (2, _('Manager')),
    (3, _('Assistant')),
)

PACKAGES = (
    (1, _('Free')),
    (2, _('Silver')),
    (3, _('Gold')),
    (4, _('Premium')),
)

STAGES = (
    (1, _('Lead')),
    (2, _('Qualified')),
    (3, _('Pending')),
    (4, _('Postponed')),
    (5, _('Contracted')),
    (6, _('Canceled')),
    (7, _('Rejected')),
)

PRODUCT = (
    (1, _('Course')),
    (2, _('Training')),
)

GENDER = (
    (1, _('Male')),
    (2, _('Female')),
)

NEXT_STEP = (
    (1, _('Follow up')),
    (2, _('Retarget')),
    (3, _('Closed')),
)

STATUS = (
    (1, _('Student')),
    (2, _('Employed')),
    (3, _('Unemployed')),
)

COUNTRY_CITIES = (
    (1, _('Abşeron (Xırdalan şəhəri)')),
    (2, _('Ağcabədi')),
    (3, _('Ağdam (Quzanlı qəsəbəsi)')),
    (4, _('Ağdaş')),
    (5, _('Ağdərə')),
    (6, _('Ağstafa')),
    (7, _('Ağsu')),
    (8, _('Astara')),
    (9, _('Babək')),
    (10, _('Balakən')),
    (11, _('Beyləqan')),
    (12, _('Bərdə')),
    (13, _('Biləsuvar')),
    (14, _('Cəbrayıl')),
    (15, _('Cəlilabad')),
    (16, _('Culfa')),
    (17, _('Daşkəsən')),
    (18, _('Füzuli')),
    (19, _('Gədəbəy')),
    (20, _('Goranboy')),
    (21, _('Göyçay')),
    (22, _('Göygöl')),
    (23, _('Hacıqabul')),
    (24, _('Xaçmaz')),
    (25, _('Xızı')),
    (26, _('Xocalı')),
    (27, _('Xocavənd')),
    (28, _('İmişli')),
    (29, _('İsmayıllı')),
    (30, _('Kəlbəcər')),
    (31, _('Kəngərli (Qıvraq qəsəbəsi)')),
    (32, _('Kürdəmir')),
    (33, _('Qax')),
    (34, _('Qazax')),
    (35, _('Qəbələ')),
    (36, _('Qobustan')),
    (37, _('Quba')),
    (38, _('Qubadlı')),
    (39, _('Qusar')),
    (40, _('Laçın')),
    (41, _('Lerik')),
    (42, _('Lənkəran')),
    (43, _('Masallı')),
    (44, _('Neftçala')),
    (45, _('Oğuz')),
    (46, _('Ordubad')),
    (47, _('Saatlı')),
    (48, _('Sabirabad')),
    (49, _('Salyan')),
    (50, _('Samux')),
    (51, _('Sədərək (Heydərabad qəsəbəsi)')),
    (52, _('Siyəzən')),
    (53, _('Şabran')),
    (54, _('Şahbuz')),
    (55, _('Şamaxı')),
    (56, _('Şəki')),
    (57, _('Şəmkir')),
    (58, _('Şərur')),
    (59, _('Şuşa')),
    (60, _('Tərtər')),
    (61, _('Tovuz')),
    (62, _('Ucar')),
    (63, _('Yardımlı')),
    (64, _('Yevlax')),
    (65, _('Zaqatala')),
    (66, _('Zəngilan')),
    (67, _('Zərdab')),
)

INDUSTRY_CHOICES = [
    (1, _('Technology')),
    (2, _('Healthcare')),
    (3, _('Finance')),
    (4, _('Education')),
    (5, _('Retail')),
    (6, _('Manufacturing')),
    (7, _('Real Estate')),
    (8, _('Entertainment')),
    (9, _('Energy')),
    (10, _('Transportation')),
    (11, _('Telecommunications')),
    (12, _('Hospitality')),
    (13, _('Construction')),
    (14, _('Legal')),
    (15, _('Agriculture')),
    (16, _('Automotive')),
    (17, _('Aerospace')),
    (18, _('Pharmaceutical')),
    (19, _('Insurance')),
    (20, _('Media')),
    (21, _('Consumer Goods')),
    (22, _('Food & Beverage')),
    (23, _('Mining')),
    (24, _('Utilities')),
    (25, _('Non-profit')),
    (26, _('Environmental')),
    (27, _('Government')),
    (28, _('Sports')),
    (29, _('Arts & Culture')),
    (30, _('Security')),
]

ORDER_STATUS = (
    (1, _('New')),
    (2, _('Qualified')),
    (3, _('Processing')),
    (4, _('Postponed')),
    (5, _('Contracted')),
    (6, _('Rejected')),
)

TASK_TYPE = (
    (1, _('Personal')),
    (2, _('Phone Call')),
    (3, _('Message')),
    (4, _('Email')),
)

PRIORITY_LEVEL = (
    (1, _('High')),
    (2, _('Medium')),
    (3, _('Low')),
)

TASK_STATUS = (
    (1, _('To Do')),
    (2, _('In Progress')),
    (3, _('Done')),
)

Event_Type = (
    (1, _('Meeting')),
    (2, _('Appointment')),
    (3, _('Event')),
)

NotificationType = (
    (1, _('Customer')),
    (2, _('Company')),
    (3, _('Order')),
    (4, _('Task')),
    (5, _('Calendar')),
)

NotificationActionType = (
    (1, _('Add')),
    (2, _('Edit')),
)

CourseStatus = (
    (1, _('Enable')),
    (0, _('Disable')),
)

DurationType = (
    (1, _('Day')),
    (2, _('Week')),
    (3, _('Month')),
)

Currency = (
    ('AZN', _('Azərbaycan Manatı')),
    ('USD', _('United States Dollar')),
    ('EUR', _('Euro')),
    ('JPY', _('Japanese Yen')),
    ('GBP', _('British Pound')),
    ('AUD', _('Australian Dollar')),
    ('CAD', _('Canadian Dollar')),
    ('CHF', _('Swiss Franc')),
    ('CNY', _('Chinese Yuan')),
    ('SEK', _('Swedish Krona')),
    ('NZD', _('New Zealand Dollar')),
    ('MXN', _('Mexican Peso')),
    ('SGD', _('Singapore Dollar')),
    ('HKD', _('Hong Kong Dollar')),
    ('NOK', _('Norwegian Krone')),
    ('KRW', _('South Korean Won')),
    ('TRY', _('Turkish Lira')),
    ('INR', _('Indian Rupee')),
    ('BRL', _('Brazilian Real')),
    ('RUB', _('Russian Ruble')),
    ('ZAR', _('South African Rand')),
    ('MYR', _('Malaysian Ringgit')),
    ('PHP', _('Philippine Peso')),
    ('IDR', _('Indonesian Rupiah')),
    ('THB', _('Thai Baht')),
    ('PLN', _('Polish Zloty')),
    ('CZK', _('Czech Koruna')),
    ('HUF', _('Hungarian Forint')),
    ('KRW', _('South Korean Won')),
    ('ILS', _('Israeli Shekel')),
    ('SAR', _('Saudi Riyal')),
    ('AED', _('United Arab Emirates Dirham')),
    ('EGP', _('Egyptian Pound')),
    ('COP', _('Colombian Peso')),
    ('VND', _('Vietnamese Dong')),
    ('NGN', _('Nigerian Naira')),
    ('PKR', _('Pakistani Rupee')),
    ('KWD', _('Kuwaiti Dinar')),
    ('QAR', _('Qatari Riyal')),
    ('OMR', _('Omani Rial')),
    ('BDT', _('Bangladeshi Taka')),
)
TicketType = (
    (1, _('Technical')),
    (2, _('Feedback')),
    (3, _('Bug Report')),
    (4, _('Feature Request')),
    (5, _('Account Issue')),
    (6, _('Billing & Payment')),
    (7, _('General Inquiry')),
)

TicketStatusType = (
    (1, _('Open')),
    (2, _('Closed')),
)

TICKET_PRIORITY_LEVEL = (
    (1, _('High')),
    (2, _('Medium')),
    (3, _('Low')),
)