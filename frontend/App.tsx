import React from 'react';
import { SQLiteProvider, SQLiteDatabase } from 'expo-sqlite';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import MainScreen from './src/screens/MainScreen';
import ProfileScreen from './src/screens/ProfileScreen';
import StatisticsScreen from './src/screens/StatisticsScreen'; 
import { RootStackParamList } from './src/types/navigation';

// Создаем стек навигаторе с нашими типами
const Stack = createNativeStackNavigator<RootStackParamList>();

async function migrateDbIfNeeded(db: SQLiteDatabase) {
  await db.execAsync(`PRAGMA journal_mode = WAL;`);
  await db.execAsync(`PRAGMA foreign_keys = ON;`);
  
  await db.execAsync(`
    CREATE TABLE IF NOT EXISTS debts (
      id TEXT PRIMARY KEY NOT NULL,
      name TEXT NOT NULL,
      amount INTEGER NOT NULL,
      is_incoming BOOLEAN DEFAULT 0
    );
  `);
}

export default function App() {
  return (
    <SQLiteProvider databaseName="splitit.db" onInit={migrateDbIfNeeded}>
      <View style={styles.container}>
        <StatusBar style="auto" />
        
        {/* Включаем контейнер навигации */}
        <NavigationContainer>
          <Stack.Navigator 
            initialRouteName="Home" 
            screenOptions={{ headerShown: false }}
          >
            <Stack.Screen name="Home" component={MainScreen} />
            <Stack.Screen name="Profile" component={ProfileScreen} />
            <Stack.Screen name="Statistics" component={StatisticsScreen} />
          </Stack.Navigator>
        </NavigationContainer>
        
      </View>
    </SQLiteProvider>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
});