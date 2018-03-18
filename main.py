#coding:utf-8

import cv2
import numpy as np

WINDOW_NAME = "captured video"
CNT = 500		# Optical Flowの最大検出数

class App :
	def __init__(self, camera=0) :
		self.camera_init(camera)

		self.frame = None
		self.pre = None
		self.now = None


	def camera_init(self, camera) :		# カメラ接続
		self.src = cv2.VideoCapture(camera)

		ret, self.frame = self.src.read()
		if not ret :
			exit("The camera cannnot get any frames.")

	def finish(self) :		# 終了処理
		self.cap.release()
		cv2.destroyAllWindows()

		exit("System is done")

	def get_Optical_Flow(self) :
		# 前フレームの特徴点取得：cv2.goodFeaturesToTrack
		# 現在フレームを使ってオプティカルフローを計算
		# 追跡に成功した特徴点情報を整理する

	def calibration(self) :		# ノイズ考慮のためのキャリブレーション
		# 一定時間，オプティカルフローを計算し続ける
		# 計算中は，フレーム内では動きがない
		# オプティカルフローのノイズを算出する

	def get_migration(self) :
		# 一定時間のオプティカルフローを検出する
		# キャリブレーションで計算したノイズと比較して，動きがあったのかどうか検出する
		# 動きがあった場合，動き開始から終了と，その前後30秒とかを保存する


	def main(self) :
		while True :
			ret, self.frame = self.src.read()		# フレーム取得









