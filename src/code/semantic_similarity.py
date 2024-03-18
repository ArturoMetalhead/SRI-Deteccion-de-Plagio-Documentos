from sklearn.metrics.pairwise import cosine_similarity

def semantic_similarity(vect_text1, vect_text2 ):
    best_sims = []

    for i in vect_text1:

        sim=[]

        for j in vect_text2:
            elem1 = i[0].reshape(1, -1)
            elem2 = j[1].reshape(1, -1)
            sim.append(cosine_similarity(i.reshape(1, -1), j.reshape(1, -1))[0][0])
        
        max_sim= max(sim)
        best_sims.append(max_sim)

    # Calcular promedio entre las mejores similitudes

    prom = sum(best_sims)/len(best_sims)

    # Devolviendo porciento de similaridad

    return prom*100