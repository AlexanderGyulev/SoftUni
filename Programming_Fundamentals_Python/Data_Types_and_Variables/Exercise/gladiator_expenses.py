lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_money_repairs_helmet = (lost_fights_count // 2) * helmet_price
total_money_repairs_sword = (lost_fights_count // 3) * sword_price
total_money_repairs_shield = (lost_fights_count // 6) * shield_price
total_money_repairs_armor = (lost_fights_count // 12) * armor_price

expenses = total_money_repairs_helmet + total_money_repairs_sword + total_money_repairs_shield + total_money_repairs_armor

print(f'Gladiator expenses: {expenses:.2f} aureus')
