import React, { useState } from 'react';
import {
  FlatList,
  NativeScrollEvent,
  NativeSyntheticEvent,
  Pressable,
  StyleSheet,
  Text,
  View,
} from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { NativeStackNavigationProp } from '@react-navigation/native-stack';
import { RootStackParamList } from '../types/navigation';

const MENU_ITEMS = ['Профиль', 'Главная', 'Статистика'];
const ITEM_HEIGHT = 60; // Фиксированная высота

export default function MenuSwiper() {
  const navigation = useNavigation<NativeStackNavigationProp<RootStackParamList>>();
  const [activeIndex, setActiveIndex] = useState(1); // По умолчанию выбрано "Мои финансы"

  // Отслеживаем свайп кнопок меню — только обновляем подсветку активного пункта,
  const handleScroll = (event: NativeSyntheticEvent<NativeScrollEvent>) => {
    const yOffset = event.nativeEvent.contentOffset.y;
    const index = Math.round(yOffset / ITEM_HEIGHT);

    if (index >= 0 && index < MENU_ITEMS.length) {
      setActiveIndex(index);
    }
  };

  // Переход на экран происходит только по явному нажатию на пункт меню
  const handlePress = (index: number) => {
    if (index === 0) {
      navigation.navigate('Profile');
    } else if (index === 2) {
      navigation.navigate('Statistics');
    }
    // index === 1 ("Мои финансы") — это текущий экран, никуда не переходим
  };

  return (
    <View style={styles.navigationWrapper}>
      <Text style={styles.arrow}>Δ</Text>

      <View style={styles.swiperContainer}>
        {/* Рамка фокуса активного элемента */}
        <View style={styles.activeIndicatorBox} />

        <FlatList
          data={MENU_ITEMS}
          keyExtractor={(item) => item}
          showsVerticalScrollIndicator={false}
          snapToInterval={ITEM_HEIGHT} // Заставляет список ровно прилипать к кнопкам
          decelerationRate="fast"
          onScroll={handleScroll}
          scrollEventThrottle={16}
          initialScrollIndex={1} // Стартуем сразу со второй кнопки ("Мои финансы")
          getItemLayout={(_, index) => ({
            length: ITEM_HEIGHT,
            offset: ITEM_HEIGHT * index,
            index,
          })}
          renderItem={({ item, index }) => {
            const isActive = index === activeIndex;
            return (
              <Pressable
                style={[styles.menuItem, { height: ITEM_HEIGHT }]}
                onPress={() => handlePress(index)}
              >
                <Text style={[styles.menuText, isActive && styles.menuTextActive]}>
                  {item}
                </Text>
              </Pressable>
            );
          }}
        />
      </View>

      <Text style={styles.arrow}>∇</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  navigationWrapper: {
    alignItems: 'center',
    marginBottom: 40,
  },
  arrow: {
    fontSize: 20,
    color: '#000',
    marginVertical: 4,
  },
  swiperContainer: {
    height: ITEM_HEIGHT, // Видна строго одна кнопка за раз
    width: '100%',
    justifyContent: 'center',
    position: 'relative',
  },
  activeIndicatorBox: {
    position: 'absolute',
    borderWidth: 2,
    borderColor: '#000',
    borderRadius: 12,
    height: 50,
    left: 0,
    right: 0,
    top: (ITEM_HEIGHT - 50) / 2,
  },
  menuItem: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  menuText: {
    fontSize: 18,
    color: '#aaa',
  },
  menuTextActive: {
    color: '#000',
    fontWeight: '600',
  },
});