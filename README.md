# Fall-detection

Fall detection project for Embedded system software course

# Coding rule:

~~~Python
local Varable: temp,tempCurrent
Global variable: TEMP
Class: TempController, People
Method: tempDisplay(*)
Every simble comes with a blank: 1 + 1 = 2, not 1+1=2 

~~~

**Each block of functionality must be represented as a class**:

~~~python
Class QLearning:
    #rewardDecay:γ, learningRate:α
    def __init__(self, actions, learningRate=0.01, rewardDecay=0.98, eGreedy=1):
        self.actions = actions  # a list
        self.Alpha = learningRate
        self.gamma = rewardDecay
        self.epsilon = eGreedy
        self.qTable = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def choose_action(self, observation):
        self.checkStateExist(observation)  #if qTable has observation
        # action selection
        if np.random.uniform() < self.epsilon:
            # choose best action
            
            stateAction = self.qTable.loc[observation, :]
            # some actions may have the same value, randomly choose on in these actions
            action = np.random.choice(stateAction[stateAction == np.max(stateAction)].index)
~~~
**Every Methods, classes must provide annotation**:

test test
