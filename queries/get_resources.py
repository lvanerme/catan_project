import psycopg2
import random

##get the resources for a player
def main():
    conn = psycopg2.connect("dbname=catan_db user=catan_user password=catan_user port=5432 host=roller.cse.taylor.edu")
    cur = conn.cursor()
    
    ##needs to pipeline to take in unique input
    resources = get_resources(cur, 1)
    print(resources)
    
    conn.commit()
    cur.close()



def get_resources(cur, p_id):
    
    cur.execute("""SELECT * FROM hand WHERE player_id = %s""", (p_id,))
    r = cur.fetchall()[0]
    result = str(r)
    result = result[1:len(result)-1]
    result = str(result).split(', ')
    resources = {'player': result[1], 'brick': result[2], 'wood': result[3], 'wheat': result[4], 'ore': result[5], 'sheep': result[6]}
    return resources

main()