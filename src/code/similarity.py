from sklearn.metrics.pairwise import cosine_similarity

def similarity(vect_text1,vect_text2):
    
    """
    Calculate the similarity between two texts using cosine similarity.

    Parameters
    ----------
    vect_text1 : list

    vect_text2 : list

    Returns
    -------
    float
    """


    # Calcular similitud coseno entre cada una de las oraciones entre documentos

    bests_sims=[]

    for i in vect_text1:

        sim=[]

        for j in vect_text2:
            sim.append(cosine_similarity(i.reshape(1, -1), j.reshape(1, -1))[0][0])
        
        max_sim= max(sim)
        bests_sims.append(max_sim)

    # Calcular promedio entre las mejores similitudes

    prom = sum(bests_sims)/len(bests_sims)

    # Devolviendo porciento de similaridad

    return prom*100