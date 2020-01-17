from distutils.core import setup
import sys
from os.path import join

p1 = str(sys.version_info[0])
p2 = str(sys.version_info[1])

site_package = 'lib/python' + p1 + '.' + p2 + '/site-packages/mocap'

setup(
    name="mocap",
    version="1.0.1",
    packages=["mocap",
              "mocap/datasets",
              "mocap/visualization",
              "mocap/math",
              "mocap/processing",
              "mocap/dataaquisition"
              ],
    data_files=[
        (join(site_package, 'data/h36m/labels'), ['mocap/data/h36m/labels/S9_walkingdog_2_label.txt.zip', 'mocap/data/h36m/labels/S7_purchases_2_label.txt.zip', 'mocap/data/h36m/labels/S8_discussion_2_label.txt.zip', 'mocap/data/h36m/labels/S9_takingphoto_1_label.txt.zip', 'mocap/data/h36m/labels/S6_smoking_1_label.txt.zip', 'mocap/data/h36m/labels/S6_directions_2_label.txt.zip', 'mocap/data/h36m/labels/S8_phoning_1_label.txt.zip', 'mocap/data/h36m/labels/S5_smoking_2_label.txt.zip', 'mocap/data/h36m/labels/S5_walkingtogether_2_label.txt.zip', 'mocap/data/h36m/labels/S6_phoning_1_label.txt.zip', 'mocap/data/h36m/labels/S7_directions_1_label.txt.zip', 'mocap/data/h36m/labels/S5_posing_2_label.txt.zip', 'mocap/data/h36m/labels/S11_smoking_2_label.txt.zip', 'mocap/data/h36m/labels/S7_walking_1_label.txt.zip', 'mocap/data/h36m/labels/S1_greeting_2_label.txt.zip', 'mocap/data/h36m/labels/S1_purchases_1_label.txt.zip', 'mocap/data/h36m/labels/S1_sitting_1_label.txt.zip', 'mocap/data/h36m/labels/S9_directions_2_label.txt.zip', 'mocap/data/h36m/labels/S8_greeting_2_label.txt.zip', 'mocap/data/h36m/labels/S11_eating_1_label.txt.zip', 'mocap/data/h36m/labels/S1_directions_1_label.txt.zip', 'mocap/data/h36m/labels/S7_waiting_1_label.txt.zip', 'mocap/data/h36m/labels/S11_phoning_2_label.txt.zip', 'mocap/data/h36m/labels/S8_sittingdown_2_label.txt.zip', 'mocap/data/h36m/labels/S9_greeting_2_label.txt.zip', 'mocap/data/h36m/labels/S5_directions_1_label.txt.zip', 'mocap/data/h36m/labels/S5_sittingdown_1_label.txt.zip', 'mocap/data/h36m/labels/S1_walking_1_label.txt.zip', 'mocap/data/h36m/labels/S5_takingphoto_2_label.txt.zip', 'mocap/data/h36m/labels/S7_sitting_2_label.txt.zip', 'mocap/data/h36m/labels/S7_phoning_2_label.txt.zip', 'mocap/data/h36m/labels/S1_directions_2_label.txt.zip', 'mocap/data/h36m/labels/S7_takingphoto_1_label.txt.zip', 'mocap/data/h36m/labels/S1_eating_1_label.txt.zip', 'mocap/data/h36m/labels/S5_waiting_2_label.txt.zip', 'mocap/data/h36m/labels/S9_directions_1_label.txt.zip', 'mocap/data/h36m/labels/S1_sittingdown_1_label.txt.zip', 'mocap/data/h36m/labels/S7_waiting_2_label.txt.zip', 'mocap/data/h36m/labels/S6_walkingdog_1_label.txt.zip', 'mocap/data/h36m/labels/S11_walkingdog_2_label.txt.zip', 'mocap/data/h36m/labels/S8_walking_2_label.txt.zip', 'mocap/data/h36m/labels/S9_smoking_2_label.txt.zip', 'mocap/data/h36m/labels/S8_walkingtogether_2_label.txt.zip', 'mocap/data/h36m/labels/S1_posing_2_label.txt.zip', 'mocap/data/h36m/labels/S6_discussion_2_label.txt.zip', 'mocap/data/h36m/labels/S9_posing_2_label.txt.zip', 'mocap/data/h36m/labels/S8_directions_2_label.txt.zip', 'mocap/data/h36m/labels/S9_sittingdown_1_label.txt.zip', 'mocap/data/h36m/labels/S11_takingphoto_1_label.txt.zip', 'mocap/data/h36m/labels/S6_posing_1_label.txt.zip', 'mocap/data/h36m/labels/S11_smoking_1_label.txt.zip', 'mocap/data/h36m/labels/S11_sitting_1_label.txt.zip', 'mocap/data/h36m/labels/S1_sittingdown_2_label.txt.zip', 'mocap/data/h36m/labels/S11_takingphoto_2_label.txt.zip', 'mocap/data/h36m/labels/S9_sitting_2_label.txt.zip', 'mocap/data/h36m/labels/S11_purchases_2_label.txt.zip', 'mocap/data/h36m/labels/S11_walkingtogether_1_label.txt.zip', 'mocap/data/h36m/labels/S1_takingphoto_1_label.txt.zip', 'mocap/data/h36m/labels/S7_posing_2_label.txt.zip', 'mocap/data/h36m/labels/S1_discussion_1_label.txt.zip', 'mocap/data/h36m/labels/S1_posing_1_label.txt.zip', 'mocap/data/h36m/labels/S6_directions_1_label.txt.zip', 'mocap/data/h36m/labels/S7_directions_2_label.txt.zip', 'mocap/data/h36m/labels/S1_takingphoto_2_label.txt.zip', 'mocap/data/h36m/labels/S5_greeting_1_label.txt.zip', 'mocap/data/h36m/labels/S1_discussion_2_label.txt.zip', 'mocap/data/h36m/labels/S7_greeting_1_label.txt.zip', 'mocap/data/h36m/labels/S5_walking_1_label.txt.zip', 'mocap/data/h36m/labels/S11_greeting_1_label.txt.zip', 'mocap/data/h36m/labels/S1_waiting_1_label.txt.zip', 'mocap/data/h36m/labels/S7_purchases_1_label.txt.zip', 'mocap/data/h36m/labels/S9_greeting_1_label.txt.zip', 'mocap/data/h36m/labels/S5_sitting_2_label.txt.zip', 'mocap/data/h36m/labels/S11_posing_2_label.txt.zip', 'mocap/data/h36m/labels/S8_directions_1_label.txt.zip', 'mocap/data/h36m/labels/S11_sitting_2_label.txt.zip', 'mocap/data/h36m/labels/S5_walkingdog_1_label.txt.zip', 'mocap/data/h36m/labels/S8_takingphoto_2_label.txt.zip', 'mocap/data/h36m/labels/S7_discussion_1_label.txt.zip', 'mocap/data/h36m/labels/S9_smoking_1_label.txt.zip', 'mocap/data/h36m/labels/S9_eating_2_label.txt.zip', 'mocap/data/h36m/labels/S9_waiting_1_label.txt.zip', 'mocap/data/h36m/labels/S11_walkingdog_1_label.txt.zip', 'mocap/data/h36m/labels/S7_smoking_1_label.txt.zip', 'mocap/data/h36m/labels/S5_sitting_1_label.txt.zip', 'mocap/data/h36m/labels/S8_sitting_2_label.txt.zip', 'mocap/data/h36m/labels/S7_eating_2_label.txt.zip', 'mocap/data/h36m/labels/S6_takingphoto_1_label.txt.zip', 'mocap/data/h36m/labels/S6_eating_1_label.txt.zip', 'mocap/data/h36m/labels/S5_sittingdown_2_label.txt.zip', 'mocap/data/h36m/labels/S6_discussion_1_label.txt.zip', 'mocap/data/h36m/labels/S8_purchases_2_label.txt.zip', 'mocap/data/h36m/labels/S8_takingphoto_1_label.txt.zip', 'mocap/data/h36m/labels/S5_smoking_1_label.txt.zip', 'mocap/data/h36m/labels/S9_walking_2_label.txt.zip', 'mocap/data/h36m/labels/S11_discussion_1_label.txt.zip', 'mocap/data/h36m/labels/S7_eating_1_label.txt.zip', 'mocap/data/h36m/labels/S8_waiting_1_label.txt.zip', 'mocap/data/h36m/labels/S6_takingphoto_2_label.txt.zip', 'mocap/data/h36m/labels/S1_greeting_1_label.txt.zip', 'mocap/data/h36m/labels/S1_smoking_2_label.txt.zip', 'mocap/data/h36m/labels/S6_walking_2_label.txt.zip', 'mocap/data/h36m/labels/S6_walkingtogether_1_label.txt.zip', 'mocap/data/h36m/labels/S6_posing_2_label.txt.zip', 'mocap/data/h36m/labels/S8_walkingtogether_1_label.txt.zip', 'mocap/data/h36m/labels/S9_purchases_1_label.txt.zip', 'mocap/data/h36m/labels/S1_walkingtogether_1_label.txt.zip', 'mocap/data/h36m/labels/S5_eating_2_label.txt.zip', 'mocap/data/h36m/labels/S6_eating_2_label.txt.zip', 'mocap/data/h36m/labels/S6_purchases_2_label.txt.zip', 'mocap/data/h36m/labels/S9_takingphoto_2_label.txt.zip', 'mocap/data/h36m/labels/S9_waiting_2_label.txt.zip', 'mocap/data/h36m/labels/S1_walkingtogether_2_label.txt.zip', 'mocap/data/h36m/labels/S11_waiting_1_label.txt.zip', 'mocap/data/h36m/labels/S9_discussion_1_label.txt.zip', 'mocap/data/h36m/labels/S6_sitting_1_label.txt.zip', 'mocap/data/h36m/labels/S5_waiting_1_label.txt.zip', 'mocap/data/h36m/labels/S6_sitting_2_label.txt.zip', 'mocap/data/h36m/labels/S6_waiting_1_label.txt.zip', 'mocap/data/h36m/labels/S11_eating_2_label.txt.zip', 'mocap/data/h36m/labels/S6_purchases_1_label.txt.zip', 'mocap/data/h36m/labels/S11_purchases_1_label.txt.zip', 'mocap/data/h36m/labels/S9_walkingdog_1_label.txt.zip', 'mocap/data/h36m/labels/S1_smoking_1_label.txt.zip', 'mocap/data/h36m/labels/S7_takingphoto_2_label.txt.zip', 'mocap/data/h36m/labels/S9_purchases_2_label.txt.zip', 'mocap/data/h36m/labels/S7_sittingdown_2_label.txt.zip', 'mocap/data/h36m/labels/S8_walkingdog_2_label.txt.zip', 'mocap/data/h36m/labels/S9_discussion_2_label.txt.zip', 'mocap/data/h36m/labels/S8_posing_1_label.txt.zip', 'mocap/data/h36m/labels/S5_walkingtogether_1_label.txt.zip', 'mocap/data/h36m/labels/S5_walkingdog_2_label.txt.zip', 'mocap/data/h36m/labels/S9_sitting_1_label.txt.zip', 'mocap/data/h36m/labels/S9_phoning_1_label.txt.zip', 'mocap/data/h36m/labels/S8_phoning_2_label.txt.zip', 'mocap/data/h36m/labels/S11_walking_1_label.txt.zip', 'mocap/data/h36m/labels/S6_sittingdown_2_label.txt.zip', 'mocap/data/h36m/labels/S6_waiting_2_label.txt.zip', 'mocap/data/h36m/labels/S9_posing_1_label.txt.zip', 'mocap/data/h36m/labels/S7_sittingdown_1_label.txt.zip', 'mocap/data/h36m/labels/S5_discussion_2_label.txt.zip', 'mocap/data/h36m/labels/S11_discussion_2_label.txt.zip', 'mocap/data/h36m/labels/S1_walking_2_label.txt.zip', 'mocap/data/h36m/labels/S5_walking_2_label.txt.zip', 'mocap/data/h36m/labels/S7_walking_2_label.txt.zip', 'mocap/data/h36m/labels/S6_sittingdown_1_label.txt.zip', 'mocap/data/h36m/labels/S8_walking_1_label.txt.zip', 'mocap/data/h36m/labels/S5_eating_1_label.txt.zip', 'mocap/data/h36m/labels/S8_greeting_1_label.txt.zip', 'mocap/data/h36m/labels/S7_walkingtogether_2_label.txt.zip', 'mocap/data/h36m/labels/S1_phoning_1_label.txt.zip', 'mocap/data/h36m/labels/S8_waiting_2_label.txt.zip', 'mocap/data/h36m/labels/S7_greeting_2_label.txt.zip', 'mocap/data/h36m/labels/S6_greeting_1_label.txt.zip', 'mocap/data/h36m/labels/S7_sitting_1_label.txt.zip', 'mocap/data/h36m/labels/S5_greeting_2_label.txt.zip', 'mocap/data/h36m/labels/S11_sittingdown_1_label.txt.zip', 'mocap/data/h36m/labels/S5_directions_2_label.txt.zip', 'mocap/data/h36m/labels/S11_sittingdown_2_label.txt.zip', 'mocap/data/h36m/labels/S6_phoning_2_label.txt.zip', 'mocap/data/h36m/labels/S9_eating_1_label.txt.zip', 'mocap/data/h36m/labels/S11_directions_2_label.txt.zip', 'mocap/data/h36m/labels/S8_discussion_1_label.txt.zip', 'mocap/data/h36m/labels/S5_posing_1_label.txt.zip', 'mocap/data/h36m/labels/S7_smoking_2_label.txt.zip', 'mocap/data/h36m/labels/S8_smoking_1_label.txt.zip', 'mocap/data/h36m/labels/S8_smoking_2_label.txt.zip', 'mocap/data/h36m/labels/S5_phoning_1_label.txt.zip', 'mocap/data/h36m/labels/S7_walkingtogether_1_label.txt.zip', 'mocap/data/h36m/labels/S6_walkingtogether_2_label.txt.zip', 'mocap/data/h36m/labels/S1_eating_2_label.txt.zip', 'mocap/data/h36m/labels/S9_walkingtogether_1_label.txt.zip', 'mocap/data/h36m/labels/S5_purchases_2_label.txt.zip', 'mocap/data/h36m/labels/S5_takingphoto_1_label.txt.zip', 'mocap/data/h36m/labels/S9_phoning_2_label.txt.zip', 'mocap/data/h36m/labels/S8_sitting_1_label.txt.zip', 'mocap/data/h36m/labels/S8_sittingdown_1_label.txt.zip', 'mocap/data/h36m/labels/S11_greeting_2_label.txt.zip', 'mocap/data/h36m/labels/S8_posing_2_label.txt.zip', 'mocap/data/h36m/labels/S1_walkingdog_1_label.txt.zip', 'mocap/data/h36m/labels/S5_discussion_1_label.txt.zip', 'mocap/data/h36m/labels/S8_eating_1_label.txt.zip', 'mocap/data/h36m/labels/S7_walkingdog_1_label.txt.zip', 'mocap/data/h36m/labels/S1_walkingdog_2_label.txt.zip', 'mocap/data/h36m/labels/S6_greeting_2_label.txt.zip', 'mocap/data/h36m/labels/S11_waiting_2_label.txt.zip', 'mocap/data/h36m/labels/S8_purchases_1_label.txt.zip', 'mocap/data/h36m/labels/S1_waiting_2_label.txt.zip', 'mocap/data/h36m/labels/S5_phoning_2_label.txt.zip', 'mocap/data/h36m/labels/S8_walkingdog_1_label.txt.zip', 'mocap/data/h36m/labels/S1_purchases_2_label.txt.zip', 'mocap/data/h36m/labels/S1_phoning_2_label.txt.zip', 'mocap/data/h36m/labels/S11_posing_1_label.txt.zip', 'mocap/data/h36m/labels/S11_directions_1_label.txt.zip', 'mocap/data/h36m/labels/S1_sitting_2_label.txt.zip', 'mocap/data/h36m/labels/S9_walkingtogether_2_label.txt.zip', 'mocap/data/h36m/labels/S8_eating_2_label.txt.zip', 'mocap/data/h36m/labels/S6_smoking_2_label.txt.zip', 'mocap/data/h36m/labels/S6_walking_1_label.txt.zip', 'mocap/data/h36m/labels/S11_walking_2_label.txt.zip', 'mocap/data/h36m/labels/S11_walkingtogether_2_label.txt.zip', 'mocap/data/h36m/labels/S7_phoning_1_label.txt.zip', 'mocap/data/h36m/labels/S5_purchases_1_label.txt.zip', 'mocap/data/h36m/labels/S7_posing_1_label.txt.zip', 'mocap/data/h36m/labels/S6_walkingdog_2_label.txt.zip', 'mocap/data/h36m/labels/S9_walking_1_label.txt.zip', 'mocap/data/h36m/labels/S7_discussion_2_label.txt.zip', 'mocap/data/h36m/labels/S9_sittingdown_2_label.txt.zip', 'mocap/data/h36m/labels/S7_walkingdog_2_label.txt.zip', 'mocap/data/h36m/labels/S11_phoning_1_label.txt.zip'])]
)
