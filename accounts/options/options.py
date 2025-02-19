from django.utils.translation import gettext_lazy as _

USERTYPE = (
    (1, 'Admin'),
    (2, 'Manager'),
)

PACKAGES = (
    (1, _("Free")),
    (2, _("Silver")),
    (3, _("Gold")),
    (4, _("Premium")),
)
STAGES = (
    (1, _("Lead")),
    (2, _("Qualified")),
    (3, _("Pending")),
    (4, _("Postponed")),
    (5, _('Contracted')),
    (6, _('Canceled')),
    (7, _('Rejected')),
)
PRODUCT = (
    (1, _("Course")),
    (2, _("Training")),
)

GENDER = (
    (1, _("Male")),
    (2, _("Female")),
)

NEXT_STEP = (
    (1, _("Follow up")),
    (2, _("Retarget")),
    (3, _("Closed"))
)

STATUS = (
    (1, _("Student")),
    (2, _("Employed")),
    (3, _("Unemployed")),
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
    (1, _("New")),
    (2, _("Qualified")),
    (3, _("Processing")),
    (4, _("Postponed")),
    (5, _('Contracted')),
    (6, _('Rejected')),
)

TASK_TYPE = (
    (1, _("Personal")),
    (2, _("Phone Call")),
    (3, _("Message")),
    (4, _("Email")),
)
PRIORITY_LEVEL = (
    (1, _("High")),
    (2, _("Medium")),
    (3, _("Low")),
)

TASK_STATUS = (
    (1, _("To Do")),
    (2, _("In Progress")),
    (3, _("Done")),
)

Event_Type = (
    (1, 'Meeting'),
    (2, 'Appointment'),
    (3, 'Event')
)
NotificationType = (
    (1, 'Customer'),
    (2, 'Company'),
    (3, 'Order'),
    (4, 'Task'),
    (5, 'Calendar'),
)
NotificationActionType = (
    (1, 'Add'),
    (2, 'Edit')
)
