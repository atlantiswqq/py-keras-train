# _*_ coding:utf-8 _*_
# Author:Atlantis
# Date:2020-01-14

import os
import ssl
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD


class KerasTrain(object):

    def __init__(self):
        self.base_dir = os.path.dirname(__file__)

    def _load_data(self):
        """关闭ssl验证"""
        ssl._create_default_https_context = ssl._create_unverified_context
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        """(60000,28*28)-->(60000,784),(10000,28*28)-->(10000,784)"""
        x_train = x_train.reshape(60000, -1) / 255
        x_test = x_test.reshape(10000, -1) / 255
        """one hot encode:5 --> [ 0, 0, 0, 0, 0,1, 0, 0, 0, 0]"""
        y_train = keras.utils.to_categorical(y_train, 10)
        y_test = keras.utils.to_categorical(y_test, 10)
        return x_train, y_train, x_test, y_test

    def _build_model(self):
        model = Sequential()
        model.add(Dense(512, activation='relu', input_shape=(784,)))
        model.add(Dense(256, activation='relu'))
        model.add(Dense(10, activation='softmax'))
        model.summary()
        model.compile(optimizer=SGD(), loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def main(self):
        target_path = os.path.join(self.base_dir, "output", "h5", "model.h5")
        x_train, y_train, x_test, y_test = self._load_data()
        model = self._build_model()
        model.fit(x_train, y_train, batch_size=64, epochs=5, validation_data=(x_test, y_test))
        score = model.evaluate(x_test, y_test)
        print("loss:", score[0])
        print("acc:", score[1])

        model.save(target_path)


if __name__ == '__main__':
    kt = KerasTrain()
    kt.main()
