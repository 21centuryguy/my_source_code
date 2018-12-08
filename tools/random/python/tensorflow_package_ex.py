import tensorflow as tf

def with_seed1():
    with tf.Graph().as_default():
        tf.set_random_seed(0)
        rand_oop1 = tf.random_normal([3])

        tf.set_random_seed(1)
        rand_oop2 = tf.random_normal([3])

        print("session1")
        with tf.Session() as sess1:
            print("op1-1 :", sess1.run(rand_oop1))
            print("op1-2 :", sess1.run(rand_oop1))
            print("op2-1 :", sess1.run(rand_oop2))
            print("op2-2 :", sess1.run(rand_oop2))

        print("\nsession2")
        with tf.Session() as sess2:
            print("op1-1 :", sess2.run(rand_oop1))
            print("op1-2 :", sess2.run(rand_oop1))
            print("op2-1 :", sess2.run(rand_oop2))
            print("op2-2 :", sess2.run(rand_oop2))
        print("\n\n")

def with_seed2():
    with tf.Graph().as_default():
        rand_oop1 = tf.random_normal([3], seed=0)
        rand_oop2 = tf.random_normal([3], seed=1)

        print("session1")
        with tf.Session() as sess1:
            print("op1-1 :", sess1.run(rand_oop1))
            print("op1-2 :", sess1.run(rand_oop1))
            print("op2-1 :", sess1.run(rand_oop2))
            print("op2-2 :", sess1.run(rand_oop2))

        print("\nsession2")
        with tf.Session() as sess2:
            print("op1-1 :", sess2.run(rand_oop1))
            print("op1-2 :", sess2.run(rand_oop1))
            print("op2-1 :", sess2.run(rand_oop2))
            print("op2-2 :", sess2.run(rand_oop2))
        print("\n\n")

def no_seed():
    with tf.Graph().as_default():
        rand_oop1 = tf.random_normal([3])
        rand_oop2 = tf.random_normal([3])

        print("session1")
        with tf.Session() as sess1:
            print("op1-1 :", sess1.run(rand_oop1))
            print("op1-2 :", sess1.run(rand_oop1))
            print("op2-1 :", sess1.run(rand_oop2))
            print("op2-2 :", sess1.run(rand_oop2))

        print("\nsession2")
        with tf.Session() as sess2:
            print("op1-1 :", sess2.run(rand_oop1))
            print("op1-2 :", sess2.run(rand_oop1))
            print("op2-1 :", sess2.run(rand_oop2))
            print("op2-2 :", sess2.run(rand_oop2))
        print("\n\n")


# with_seed1()

# with_seed2()

no_seed()
