from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class FrogBossAssets: 


	# Image Rule Assets
	# 左边竞猜 
	I_BET_LEFT = RuleImage(roi_front=(88,342,145,100), roi_back=(88,342,145,100), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_bet_left.png")
	# 右边竞猜 
	I_BET_RIGHT = RuleImage(roi_front=(1044,344,146,100), roi_back=(1044,344,146,100), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_bet_right.png")
	# description 
	I_BET_SUCCESS_BOX = RuleImage(roi_front=(590,439,87,50), roi_back=(590,439,87,50), threshold=0.75, method="Template matching", file="./tasks/FrogBoss/fb/fb_bet_success_box.png")
	# 左边赢了 
	I_SUCCESS_LEFT = RuleImage(roi_front=(108,352,100,100), roi_back=(108,352,100,100), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_success_left.png")
	# 右边输了 
	I_FAILURE_RIGHT = RuleImage(roi_front=(1067,341,100,100), roi_back=(1067,341,100,100), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_failure_right.png")
	# description 
	I_NEXT_COMPETITION = RuleImage(roi_front=(1098,510,42,36), roi_back=(1098,510,42,36), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_next_competition.png")
	# 30万金币 
	I_GOLD_30 = RuleImage(roi_front=(824,499,78,76), roi_back=(824,499,78,76), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_gold_30.png")
	# 确认竞猜 
	I_BET_SURE = RuleImage(roi_front=(1014,404,100,100), roi_back=(1014,404,100,100), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_bet_sure.png")
	# description 
	I_GOLD_30_CHECK = RuleImage(roi_front=(512,180,68,83), roi_back=(402,141,459,489), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_gold_30_check.png")
	# description 
	I_BETTED = RuleImage(roi_front=(93,352,125,54), roi_back=(49,322,1192,100), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_betted.png")
	# description 
	I_SUCCESS_RIGHT = RuleImage(roi_front=(1061,336,122,116), roi_back=(1061,336,122,116), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_success_right.png")
	# description 
	I_FAILURE_LEFT = RuleImage(roi_front=(107,351,100,100), roi_back=(107,351,100,100), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_failure_left.png")
	# description 
	I_BET_FAILURE = RuleImage(roi_front=(510,266,269,72), roi_back=(510,266,269,72), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_bet_failure.png")
	# description 
	I_BET_SUCCESS = RuleImage(roi_front=(512,264,260,73), roi_back=(433,214,418,151), threshold=0.8, method="Template matching", file="./tasks/FrogBoss/fb/fb_bet_success.png")


	# Image Rule Assets
	# description 
	I_FROG_BOSS_ENTER = RuleImage(roi_front=(1191,391,36,38), roi_back=(1174,135,78,320), threshold=0.7, method="Template matching", file="./tasks/FrogBoss/fb/fb_frog_boss_enter.png")


	# Ocr Rule Assets
	# Ocr-description 
	O_LEFT_COUNT = RuleOcr(roi=(144,541,69,31), area=(144,541,69,31), mode="Digit", method="Default", keyword="", name="left_count")
	# Ocr-description 
	O_RIGHT_COUNT = RuleOcr(roi=(1110,542,77,32), area=(1110,542,77,32), mode="Digit", method="Default", keyword="", name="right_count")
	# Ocr-description 
	O_TIME_REMAIN = RuleOcr(roi=(590,601,91,35), area=(590,601,91,35), mode="Duration", method="Default", keyword="", name="time_remain")


