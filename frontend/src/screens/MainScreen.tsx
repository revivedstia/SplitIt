import React, { useEffect, useState } from 'react';
import {
  FlatList,
  NativeScrollEvent,
  NativeSyntheticEvent,
  StyleSheet,
  Text,
  View,
} from 'react-native';
import { useSQLiteContext } from 'expo-sqlite';
import { useNavigation } from '@react-navigation/native';
import { NativeStackNavigationProp } from '@react-navigation/native-stack';
import { RootStackParamList } from '../types/navigation';

type Debt = { id: string; name: string; amount: number; is_incoming: number };

const MENU_ITEMS = ['Профиль', 'Мои финансы', 'Статистика'];
const ITEM_HEIGHT = 60; // Фиксированная высота кнопки для свайпера

export default function MainScreen() {
  const navigation = useNavigation<NativeStackNavigationProp<RootStackParamList>>();
  const db = useSQLiteContext(); //
  const [debts, setDebts] = useState<Debt[]>([]);
  const [activeIndex, setActiveIndex] = useState(1); // По умолчанию выбрано "Мои финансы"

  // Загрузка данных о долгах
  const loadDebts = async () => {
    const result = await db.getAllAsync('SELECT * FROM debts;');
    setDebts(result as Debt[]);
  };

  useEffect(() => {
    loadDebts();
  }, [db]);

  // Считаем общую сумму, которую МЫ задолжали (is_incoming = 0)
  const totalOwed = debts
    .filter((d) => d.is_incoming === 0)
    .reduce((sum, item) => sum + item.amount, 0);

  // Фильтруем тех, кто должен НАМ (is_incoming = 1)
  const incomingDebts = debts.filter((d) => d.is_incoming === 1);

  // Отслеживаем свайп кнопок меню
  const handleScroll = (event: NativeSyntheticEvent<NativeScrollEvent>) => {
    const yOffset = event.nativeEvent.contentOffset.y;
    const index = Math.round(yOffset / ITEM_HEIGHT);
    
    if (index >= 0 && index < MENU_ITEMS.length) {
      setActiveIndex(index);
      
      // Переключаем экраны при свайпе меню
      if (index === 0) {
        // Чтобы свайп не срабатывал мгновенно во время инерции, 
        // переключаем экран с микро-задержкой после фиксации
        setTimeout(() => navigation.navigate('Profile'), 200);
      } else if (index === 2) {
        setTimeout(() => navigation.navigate('Statistics'), 200);
      }
    }
  };

  return (
    <View style={styles.screen}>
      {/* Шапка приветствия */}
      <View style={styles.header}>
        <Text style={styles.greeting}>Приветик,</Text>
        <Text style={styles.username}>Username!</Text>
      </View>

      {/* Блок твоего текущего баланса */}
      <View style={styles.balanceSection}>
        <Text style={styles.sectionTitle}>Ваш баланс на сегодня:</Text>
        <Text style={styles.debtText}>
          Вы задолжали <Text style={styles.boldText}>{totalOwed}</Text> рублей
        </Text>
      </View>

      {/* Блок списка должников */}
      <View style={styles.debtorsSection}>
        <Text style={styles.sectionTitle}>Вам еще не скинули:</Text>
        {incomingDebts.map((item) => (
          <Text key={item.id} style={styles.debtorRow}>
            {item.name} <Text style={styles.boldText}>{item.amount}</Text> рублей
          </Text>
        ))}
      </View>

      {/* Интерактивный вертикальный свайпер кнопок (меню) */}
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
                <View style={[styles.menuItem, { height: ITEM_HEIGHT }]}>
                  <Text style={[styles.menuText, isActive && styles.menuTextActive]}>
                    {item}
                  </Text>
                </View>
              );
            }}
          />
        </View>

        <Text style={styles.arrow}>∇</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: 80,
    paddingHorizontal: 40,
  },
  header: {
    marginBottom: 40,
  },
  greeting: {
    fontSize: 32,
    fontFamily: 'System',
    color: '#000',
  },
  username: {
    fontSize: 32,
    fontWeight: 'bold',
    fontFamily: 'System',
    color: '#000',
  },
  balanceSection: {
    marginBottom: 35,
  },
  sectionTitle: {
    fontSize: 18,
    color: '#333',
    marginBottom: 8,
  },
  debtText: {
    fontSize: 18,
    color: '#000',
  },
  debtorsSection: {
    flex: 1,
  },
  debtorRow: {
    fontSize: 18,
    marginVertical: 4,
    color: '#000',
  },
  boldText: {
    fontWeight: 'bold',
  },
  /* Стилизация свайп-барабана */
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