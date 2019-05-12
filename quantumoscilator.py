#%%
import numpy as np
import copy


def harmonic_oscillators(N, E, t):
    #initiallize oscilators
    oscillators = np.zeros(N)
    oscillators[0] = E
    #print(oscillators)

    #loop over t steps
    for step in range(t):

        #take a trial move
        oscillators_trial = copy.deepcopy(oscillators)

        #randomly exchange energy
        A =  np.random.randint(0, high=N)
        B =  np.random.randint(0, high=N)
        oscillators_trial[A] = oscillators_trial[A]+1
        oscillators_trial[B] = oscillators_trial[B]-1

        #test if move is unphysical and reject
        if any(i < 0 for i in oscillators_trial):
            continue

        #accept move
        oscillators =  copy.deepcopy(oscillators_trial)
    
    return(oscillators)

num_oscillators = 50
total_energy = 50
#eq_oscillators =  harmonic_oscillators(num_oscillators,total_energy,1000000)

#plt results
import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
starting_oscillators = np.zeros(num_oscillators)
starting_oscillators[0] = total_energy
# plt.bar(np.arange(num_oscillators)+1, starting_oscillators)
# # plt.xticks(np.arange(num_oscillators)+1)
# # plt.yticks(np.arange(total_energy))
# plt.xlabel("oscillator")
# plt.ylabel("energy / $\hbar w$")
# plt.savefig("./starting_oscillatorexample.png")

# eq_oscillators =  harmonic_oscillators(num_oscillators,total_energy,1000000)
# plt.bar(np.arange(num_oscillators)+1, eq_oscillators,color="C1")
# # plt.xticks(np.arange(num_oscillators)+1)
# # plt.yticks(np.arange(total_energy))
# plt.xlabel("oscillator")
# plt.ylabel("energy / $\hbar w$")
# plt.savefig("./final_oscillatorexample.png")

#get probability dist
# prob_state = []
# for ek in range(total_energy):
#     count = (eq_oscillators == ek).sum()
#     prob_state.append(count/num_oscillators)

# #plt.hist(prob_state)


# plt.plot(np.arange(total_energy), prob_state, 'o')
# plt.ylabel("probability / $P (k)$")
# plt.xlabel("energy / $\hbar w$")
# plt.savefig("energy_probabilities.png")

# S = -1*num_oscillators*np.nansum(prob_state*np.log(prob_state))
# print(S)

from scipy.misc import factorial
omega = factorial(num_oscillators+total_energy-1)/(factorial(num_oscillators-1)*factorial(total_energy))
print(np.log(omega))

# plt.plot(count_state, np.exp(np.arange(total_energy)))

#calculate entropy
#probs_state = prob_state[prob_state != 0.0]
# print(prob_state)


#%% Simulate time dependence of entropy

S = []
for steps in np.logspace(0,5):
    eq_oscillators =  harmonic_oscillators(num_oscillators,total_energy,int(steps))
    count_state = []
    prob_state = []
    for ek in range(total_energy):
        count = (eq_oscillators == ek).sum()
        count_state.append(count)
        prob_state.append(count/num_oscillators)
    S.append(-1*num_oscillators*np.nansum(prob_state*np.log(prob_state)))

plt.semilogx(np.logspace(0,5), S)
plt.xlabel("timestep")
plt.ylabel("$S$")
plt.savefig("./time.png", dpi=600)


