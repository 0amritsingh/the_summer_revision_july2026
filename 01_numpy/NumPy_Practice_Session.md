# NumPy — Practice Session

**Date/Time:** Thursday, 16 July 2026, 04:40 PM

**Topic:** NumPy (from uploaded PDF — 03-Numpy-Handbook.pdf)

**Source:** Questions built strictly from the uploaded material (arrays, shape/dtype, reshaping, indexing/slicing, fancy indexing & boolean masking, axes, data types, broadcasting, vectorization, built-in math functions).

## Directions Followed

1. **Concepts** — strengthen core concepts, especially ones beginners get stuck on

2. **Analytical and Critical Thinking** — real-life scenario / case-study style questions

3. **Reasoning** — questions involving maths to test reasoning ability

4. **Interview Questions** — commonly-stuck-on interview questions (researched online, scoped to this material)

## Format

4 sections × (3 Easy + 3 Medium + 3 Hard + 1 Impossible) = 10 per section, **40 total**.

Hints appear only at the end, only for Medium/Hard/Impossible (none for Easy), kept brutal/minimal.

**No answers included anywhere.**

---

## Section 1: Concept Questions

**Easy**

1. What is the key structural difference between how a Python list and a NumPy array store their elements in memory?

2. Which NumPy function creates a 4×4 identity matrix?

3. What does `arr.ndim` return for the array `np.array([[1,2],[3,4]])`?

**Medium**

4. Why is `arr.astype(np.int32)` sometimes done even though it can lose precision?

5. Explain what "homogeneous" means for a NumPy array and how it differs from a Python list in this respect.

6. What is the difference between `.flatten()` and `.reshape()`?

**Hard**

7. Why does slicing a NumPy array return a *view* instead of a copy, and what problem could this cause if not handled carefully?

8. Explain the two-part condition NumPy checks to decide if two arrays can be broadcast together.

9. Why is `dtype='object'` discouraged in NumPy even though it allows mixed data types?

**Impossible**

10. Explain, at the level of memory layout and CPU instructions, why SIMD allows vectorized NumPy operations to outperform an equivalent Python `for` loop.

---

## Section 2: Analytical and Critical Thinking

**Easy**

1. You load 1 million sensor readings into a Python list vs a NumPy array. Which will use more memory, and why?

2. You have a 2D array of shape (2,3) representing 2 sheets... wait — actually you have `arr = np.array([[1,2,3],[4,5,6]])`. A colleague wants only the last two columns of both rows. Which slicing expression achieves this?

3. You want to check if any value in an array of exam scores exceeds 90. What NumPy technique from the material would you use?

**Medium**

4. A dataset has 5 samples and 3 features, stored as a (5,3) array. Your teammate calls `data.mean(axis=0)` expecting the average score per *sample*, but gets the average per *feature* instead. What did they misunderstand about axes?

5. You slice `sub = arr[1:3]` and modify `sub[0] = 999`, and the original array changes too. Your teammate is confused because Python list slicing doesn't behave this way. How would you explain this to them, and what should they do instead if they wanted an independent copy?

6. You're filtering a large array to keep only values greater than 50. One teammate suggests a `for` loop with `if` checks; another suggests boolean masking. Which is better for a 10-million-element array, and why?

**Hard**

7. You have a 3D array of shape (2,2,3) representing 2 "sheets" of 2×3 data. Design an indexing expression to extract the second row from every sheet, and explain why the result has the shape it does.

8. A downcast from `int64` to `int32` silently changes some values in your dataset. Diagnose what likely happened and why NumPy didn't raise an error.

9. You add a (2,3) array and a (3,) array and it works, but adding a (2,3) array and a (2,) array fails. Explain, using broadcasting rules, exactly why one succeeds and the other doesn't.

**Impossible**

10. You're building a normalization pipeline (subtract mean, divide by std, per feature) for a live ML system processing millions of rows per second. Critically evaluate where broadcasting helps performance versus where it could still become a memory or precision bottleneck, and what dtype/axis decisions you'd need to justify.

---

## Section 3: Reasoning Ability

**Easy**

1. Given `arr = np.arange(1, 10, 2)`, list out all the elements it produces.

2. If `arr = np.array([10,20,30,40,50])`, what does `arr[::2]` produce?

3. For `np.linspace(0, 1, 5)`, what is the spacing between each consecutive value?

**Medium**

4. Given `arr = np.array([[1,2,3],[4,5,6],[7,8,9]])`, compute `np.sum(arr, axis=0)` and `np.sum(arr, axis=1)` by hand.

5. If `arr_int64 = np.array([1,2,3], dtype=np.int64)`, how many total bytes does `arr_int64.nbytes` report, and how did you calculate it?

6. Given `arr = np.array([10,20,30,40,50])` and `idx = [0,2,4]`, what does `arr[idx]` return?

**Hard**

7. A dataset `data` has shape (5,3). Compute `mean = data.mean(axis=0)` and `std = data.std(axis=0)` conceptually — walk through what shape `mean` and `std` will have, and how broadcasting applies them back across all 5 rows in `(data - mean) / std`.

8. Given `arr3D` of shape (2,2,3), reason out the exact shape of `arr3D[:, 0, :]` and list what values it would contain if `arr3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])`.

9. If reshaping a 1D array of size 9 into a 2D array, list every valid (rows, columns) shape pair possible, and explain why (2,5) is invalid.

**Impossible**

10. You have an array of shape (4,5) and want to reshape it into a 3D array without knowing one of the dimensions in advance. Reason through how `-1` would be used in `.reshape()` for this (even though not explicitly shown in the material, infer it from how shape and size relate), and what constraint must hold for it to work.

---

## Section 4: Interview Challenging Questions

**Easy**

1. In an interview, you're asked: "Why would you choose NumPy over a Python list for numerical work?" What three reasons from the material would you give?

2. "What does `.shape` tell you about a NumPy array?" — answer concisely as you would in an interview.

3. "How do you check the data type of a NumPy array?" — give the exact attribute name.

**Medium**

4. "What is the difference between `np.array()` and `np.arange()`?" — explain as if answering live.

5. "Explain vectorization in NumPy and why it matters for performance." — structure your answer as Concept → Example → Benefit.

6. "What's the difference between indexing and slicing in NumPy, and why does slicing behavior surprise people coming from Python lists?"

**Hard**

7. "Explain broadcasting rules in NumPy with an example involving a 2D and a 1D array." — be ready to justify why it works, not just what happens.

8. "How would you reduce the memory footprint of a large NumPy array without losing critical data precision?"

9. "Walk me through how you'd normalize a dataset (mean 0, std 1) per feature using only NumPy operations, no loops."

**Impossible**

10. "You're processing a live stream of sensor data as NumPy arrays, and a downstream model keeps getting corrupted values after a `.astype()` conversion. Walk me through your full debugging process, from checking dtypes to axis assumptions to broadcasting mismatches, and explain how you'd prevent this class of bug going forward."

---

## Hints

*(Hints given only where necessary — brutal and minimal. Easy questions have none.)*

**Section 1**

- Q4: Think about `arr.nbytes` before and after.

- Q5: Compare with Python's `list = [1, "a", 3.5]`.

- Q6: One always returns 1D.

- Q7: Think shared memory buffer.

- Q8: Trailing dimensions.

- Q9: Think what `dtype='object'` actually stores — pointers.

- Q10: Think "one instruction, many data lanes."

**Section 2**

- Q4: Axis 0 moves *down* — across which dimension?

- Q5: `.copy()`.

- Q6: Think function call overhead per element.

- Q7: Middle index is fixed, others are `:`.

- Q8: int32 has a smaller max value than int64.

- Q9: Trailing dimension of (2,) vs (3,) against a (2,3) array.

- Q10: Consider dtype precision vs memory tradeoffs at scale.

**Section 3**

- Q4: Axis 0 = down columns, axis 1 = across rows.

- Q5: 3 elements × 8 bytes.

- Q6: Order follows the index list exactly.

- Q7: `mean`/`std` will be shape (3,) — broadcast against (5,3).

- Q8: `:,0,:` fixes the middle axis only.

- Q9: Factors of 9 only.

- Q10: `-1` tells NumPy to infer that dimension from total size.

**Section 4**

- Q5: Structure literally as three labeled parts.

- Q6: Views vs copies.

- Q7: Check trailing dimension compatibility.

- Q8: Downcasting dtype, e.g. int64 → int32.

- Q9: `(data - data.mean(axis=0)) / data.std(axis=0)`.

- Q10: Check dtype range, axis argument, and broadcast shape at every step.
