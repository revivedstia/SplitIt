import React, { useEffect, useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { useSQLiteContext } from 'expo-sqlite';
import MenuSwiper from '../components/MenuSwiper';

type Debt = { id: string; name: string; amount: number; is_incoming: boolean };

export default function MainScreen() {
  const navigation = useNavigation<NativeStackNavigationProp<RootStackParamList>>();
  const db = useSQLiteContext(); 
  const [debts, setDebts] = useState<Debt[]>([]);

  // Загрузка данных о долгах
  const loadDebts = async () => {
    const result = await db.getAllAsync('SELECT * FROM debts;');
    setDebts(result as Debt[]);
  };

  useEffect(() => {
    loadDebts();
  }, [db]);

  // Считаем общую сумму, которую МЫ задолжали 
  const totalOwed = debts
    .filter((d) => d.is_incoming === false)
    .reduce((sum, item) => sum + item.amount, 0);

  // Фильтруем тех, кто должен НАМ
  const incomingDebts = debts.filter((d) => d.is_incoming === true);

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

      {/* Меню-свайпер вынесен в отдельный компонент */}
      <MenuSwiper />
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
});