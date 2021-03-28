# GPCR-KD

This code is GPCR-KD's Program.

## Abstract

### Motivation

A significant number of machine learning-based algorithms have been developed for the classification of G-protein-coupled receptors (GPCRs) as the function prediction of newly discovered and incremental large-scale GPCRs has been a hotspot in biological research. The high accuracy in these prior studies reveals that extracting valuable features and filtering out redundancy are key challenges to determining overall accuracy. To get a more efficient model, this study further considers the case of feature synonyms and puts forward a new method based on functional word clustering and integration. The essence behind this method is the novel feature-knowledge-mining strategy. Unlike prior studies, the proposed strategy adds a layer between the extracted features and classifiers to evaluate the independence of each candidate feature using an evolutionary hypothesis based on residue substitution matrices, clustering candidate features, and integrating them by choosing the main functional words. These words are the final features and are used to compose a feature knowledge base. GPCR sequences are then transferred into feature vectors by the knowledge base and used by classifiers.

### Results

The study classified 12,731 GPCR sequences. Four classic machine-learning algorithms—Naïve Bayesian (NB), Random Forest (SF), Supporting Vector Machine (SVM), and Multi-Layer Perception (MLP)—were adopted to perform the classification on all GPCR class levels. Surprisingly, the novel feature-knowledge-mining strategy helped all classifiers achieve significant improvement in all test cases. Specifically, the MLP-based neural network classifier achieved an average accuracy of 99.84%, 99.69%, 99.49%, and 98.19% at the family level, subfamily level (level I), sub-subfamily level (level II), and subtype level (level III), respectively. Compared to the prior methods using identical dataset, the classification error is reduce.


### User Guide
If you are the first time to use this program, please download the code and choose folder "seqToResult" and follow the readme in it.
